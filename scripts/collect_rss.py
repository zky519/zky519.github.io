"""RSS publisher: source-provided excerpts only, no generated claims or API keys."""
import concurrent.futures as cf
import datetime as dt
import email.utils
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

TARGETS = {'ai': 5, 'politics_economy': 5, 'games': 5, 'f1': 2}
SOURCES = [
 ('IT之家','https://www.ithome.com/rss/','ai','china'),
 ('Solidot','https://www.solidot.org/index.rss','ai','china'),
 ('TechCrunch AI','https://techcrunch.com/category/artificial-intelligence/feed/','ai','international'),
 ('NVIDIA','https://blogs.nvidia.com/feed/','ai','international'),
 ('BBC World','https://feeds.bbci.co.uk/news/world/rss.xml','politics_economy','international'),
 ('BBC Business','https://feeds.bbci.co.uk/news/business/rss.xml','politics_economy','international'),
 ('BBC Asia','https://feeds.bbci.co.uk/news/world/asia/rss.xml','politics_economy','asia_pacific'),
 ('BBC Technology','https://feeds.bbci.co.uk/news/technology/rss.xml','politics_economy','international'),
 ('人民网财经','http://www.people.com.cn/rss/finance.xml','politics_economy','china'),
 ('GamesRadar','https://www.gamesradar.com/feeds/all/','games','international'),
 ('PC Gamer','https://www.pcgamer.com/rss/','games','international'),
 ('Motorsport F1','https://www.motorsport.com/rss/f1/news/','f1','international'),
 ('Autosport F1','https://www.autosport.com/rss/f1/news/','f1','international'),
]
AI = re.compile(r'\bAI\b|artificial intelligence|GPU|data cent|CUDA|NVIDIA|人工智能|大模型|算力|英伟达|数据中心|智能体|DeepSeek|通义|模型',re.I)
TECH = re.compile(r'chip|tech|AI|energy|digital|semiconductor|芯片|科技|数字|能源|人工智能',re.I)
GAME = re.compile(r'witcher|skyrim|resident evil|gta|grand theft|elden ring|baldur|cyberpunk|final fantasy|monster hunter|civilization|fable|persona|metaphor|assassin|hollow knight|silksong|pokemon|zelda|mario|honkai|genshin|game|rpg',re.I)
EXCLUDE = re.compile(r'best .*deals|coupon|discount code|graphics card|gaming laptop|gaming chair|monitor deal|headset|best .*TV|Fortnite|Valorant|Counter.Strike|League of Legends',re.I)

def clean(s):
    s=re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', s or '', flags=re.S|re.I)
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', s))).strip()

def parse_date(value):
    try:
        t=email.utils.parsedate_to_datetime(value)
    except (ValueError, TypeError):
        try: t=dt.datetime.fromisoformat(value.replace('Z','+00:00'))
        except (ValueError, TypeError): return None
    return t.replace(tzinfo=dt.timezone.utc) if t.tzinfo is None else t

def parse_feed(raw, source, now):
    name,url,category,region=source
    root=ET.fromstring(raw)
    entries=root.findall('.//item') or root.findall('.//{http://www.w3.org/2005/Atom}entry')
    out=[]
    for e in entries:
        fields={c.tag.split('}')[-1]: c.text or '' for c in e}
        title=clean(fields.get('title',''))
        link=fields.get('link','').strip()
        if not link:
            for c in e:
                if c.tag.endswith('link') and c.attrib.get('rel','alternate')=='alternate':
                    link=c.attrib.get('href','');break
        date=parse_date(fields.get('pubDate') or fields.get('published') or fields.get('updated'))
        if not title or not link.startswith(('https://','http://')) or date is None: continue
        if not dt.timedelta(0)<=now-date<=dt.timedelta(hours=72): continue
        summary=clean(fields.get('description') or fields.get('summary') or fields.get('encoded') or fields.get('content'))
        text=title+' '+summary
        if category=='ai' and not AI.search(text): continue
        if category=='games' and (not GAME.search(text) or EXCLUDE.search(title)): continue
        out.append(dict(title=title,summary=summary[:500] or '来源未提供简介，请点击标题阅读原文。',category=category,source_name=name,source_url=link.split('#')[0],published_at=date.isoformat(),region=region,is_tech_related=bool(TECH.search(text)),game_type='unspecified' if category=='games' else None,verification='rss_source_excerpt',ready_for_publication=True,why_it_matters='来源简介；未经独立事实核查，不含AI生成分析。'))
    return out

def fetch(source,now):
    req=urllib.request.Request(source[1],headers={'User-Agent':'DailyNewsRSS/1.0 (+https://zky519.github.io)'})
    with urllib.request.urlopen(req,timeout=25) as r: raw=r.read(4_000_001)
    if len(raw)>4_000_000: raise ValueError('feed too large')
    return parse_feed(raw,source,now)

def select(candidates,now):
    result=[];seen=set();titles=set()
    for cat,target in TARGETS.items():
        pool=sorted([x for x in candidates if x['category']==cat],key=lambda x:x['published_at'],reverse=True)
        chosen=[]
        def take(predicate, count):
            for x in pool:
                key=re.sub(r'\W+','',x['title']).lower()
                if len(chosen)>=target or count<=0: break
                if x['source_url'] in seen or key in titles or not predicate(x): continue
                chosen.append(x);seen.add(x['source_url']);titles.add(key);count-=1
        # Soft geographic/technology preferences; fill remaining slots by recency.
        if cat in ('ai','politics_economy'): take(lambda x:x['region']=='china',2)
        if cat=='politics_economy':
            take(lambda x:x['region']=='asia_pacific',1)
            take(lambda x:x['is_tech_related'],3-sum(x['is_tech_related'] for x in chosen))
        take(lambda x:now-parse_date(x['published_at'])<=dt.timedelta(hours=24),target-len(chosen))
        take(lambda x:True,target-len(chosen))
        result.extend(chosen)
    return result

def main():
    now=dt.datetime.now(dt.timezone(dt.timedelta(hours=8)))
    candidates=[];errors=[]
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        futures={ex.submit(fetch,s,now):s for s in SOURCES}
        for f,s in futures.items():
            try: candidates.extend(f.result())
            except Exception as e: errors.append({'source':s[0],'error':type(e).__name__})
    items=select(candidates,now)
    counts={c:sum(x['category']==c for x in items) for c in TARGETS}
    report=dict(schema_version=1,date=now.date().isoformat(),collected_at=now.isoformat(),status='ready_for_publication',mode='rss_excerpt',counts=counts,shortfalls={c:n-counts[c] for c,n in TARGETS.items() if counts[c]<n},items=items,notice='RSS来源简介，保留原文语言；未经独立事实核查。')
    Path('rss-run-log.json').write_text(json.dumps(dict(counts=counts,candidates=len(candidates),errors=errors),ensure_ascii=False,indent=2))
    if len(items)<14 or any(counts[c]<TARGETS[c]/2 for c in TARGETS):
        sys.exit('Insufficient feed coverage; previous website data preserved. See rss-run-log.json')
    p=Path('daily');p.mkdir(exist_ok=True)
    path=p/(report['date']+'.json');path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    Path('rss-report-path.txt').write_text(str(path))
    print(json.dumps(counts))
if __name__=='__main__': main()
