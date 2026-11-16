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
ROOT = Path(__file__).resolve().parent.parent
SOURCES = [x for x in json.loads((ROOT/'config/rss-sources.json').read_text()) if x['status']=='enabled']
AI = re.compile(r'\bAI\b|artificial intelligence|GPU|data cent|CUDA|NVIDIA|人工智能|大模型|算力|英伟达|数据中心|智能体|DeepSeek|通义|模型',re.I)
TECH = re.compile(r'chip|tech|AI|energy|digital|semiconductor|芯片|科技|数字|能源|人工智能',re.I)
GAME = re.compile(r'游戏|遊戲|重制|重製|塞尔达|薩爾達|肉肉男孩|单机|單機|生化危机|最终幻想|怪物猎人|巫师|赛博朋克|艾尔登|空洞骑士|宝可梦|黑神话|明末|Steam|PlayStation|Xbox|witcher|skyrim|resident evil|gta|grand theft|elden ring|baldur|cyberpunk|final fantasy|monster hunter|civilization|fable|persona|metaphor|assassin|hollow knight|silksong|pokemon|zelda|mario|honkai|genshin|game|rpg',re.I)
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
    if isinstance(source,dict):
        name,url,category,region=(source[k] for k in ('name','url','category','region'))
    else:
        name,url,category,region=source
        source={'source_language':'zh' if name=='机核' else 'en','publisher_id':name.lower()}
    root=ET.fromstring(raw)
    entries=root.findall('.//item') or root.findall('.//{http://www.w3.org/2005/Atom}entry') or root.findall('.//{http://purl.org/rss/1.0/}item')
    out=[]
    for e in entries:
        fields={c.tag.split('}')[-1]: c.text or '' for c in e}
        title=clean(fields.get('title',''))
        link=fields.get('link','').strip()
        if not link:
            for c in e:
                if c.tag.endswith('link') and c.attrib.get('rel','alternate')=='alternate':
                    link=c.attrib.get('href','');break
        date=parse_date(fields.get('pubDate') or fields.get('published') or fields.get('updated') or fields.get('date'))
        if not title or not link.startswith(('https://','http://')) or date is None: continue
        if not dt.timedelta(0)<=now-date<=dt.timedelta(hours=72): continue
        summary=clean(fields.get('description') or fields.get('summary') or fields.get('encoded') or fields.get('content'))
        text=title+' '+summary
        if category=='ai' and not AI.search(title): continue
        if category=='games' and (not GAME.search(title) or EXCLUDE.search(title) or re.search(r'Avengers|Disney Plus|Marvel|TV series|movie|Jensen Huang|affair|Nvidia CEO|电影|電影|影视|影視|八卦|手游电竞|电竞赛事',title,re.I)): continue
        if category=='f1' and not re.search(r'赛车|賽車|大奖赛|大獎賽|维斯塔潘|汉密尔顿|法拉利|F1|Formula 1|Grand Prix|Verstappen|Hamilton|Russell|Antonelli|Piastri|Leclerc|Norris|Wolff|Ferrari|Red Bull|Mercedes',title,re.I): continue
        if category=='f1' and re.search(r'auction|road car|Stirling Moss|SLR McLaren',title,re.I): continue
        out.append(dict(title=title,summary=summary[:500] or '来源未提供简介，请点击标题阅读原文。',category=category,source_name=name,source_language=source['source_language'],publisher_id=source['publisher_id'],feed_url=url,source_url=link.split('#')[0],published_at=date.isoformat(),region=region,is_tech_related=bool(TECH.search(text)),game_type='unspecified' if category=='games' else None,verification='rss_source_excerpt',ready_for_publication=True,why_it_matters=''))
    return out

def fetch(source,now):
    req=urllib.request.Request(source['url'],headers={'User-Agent':'DailyNewsRSS/1.0 (+https://zky519.github.io)'})
    with urllib.request.urlopen(req,timeout=12) as r: raw=r.read(4_000_001)
    if len(raw)>4_000_000: raise ValueError('feed too large')
    return parse_feed(raw,source,now)

def select(candidates,now):
    from collections import Counter
    result=[];seen=set();titles=set();global_counts=Counter()
    # Scarce F1 first. Every channel from a publisher shares these caps.
    for cat in ('f1','ai','politics_economy','games'):
        target=TARGETS[cat];chosen=[];local=Counter()
        pool=[x for x in candidates if x['category']==cat and parse_date(x['published_at']) and dt.timedelta(0)<=now-parse_date(x['published_at'])<=dt.timedelta(hours=72)]
        while len(chosen)<target:
            eligible=[]
            for x in pool:
                pub=x.get('publisher_id',x.get('source_name',x['source_url']))
                key=re.sub(r'\W+','',x['title']).lower()
                if x['source_url'] in seen or key in titles or global_counts[pub]>=3 or local[pub]>=(1 if cat=='f1' else 2):continue
                def score(x):
                    region=x.get('region');china=sum(y.get('region')=='china' for y in chosen)
                    region_bonus=2 if region=='china' and china<2 else 2 if region in ('international','asia_pacific') and len(chosen)-china<3 else 0
                    return (x.get('source_language')=='zh',-local[pub],region_bonus+(2 if region=='asia_pacific' and cat=='politics_economy' else 0),bool(x.get('is_tech_related')),parse_date(x['published_at']))
                eligible.append((score(x),x,pub,key))
            if not eligible:break
            _,x,pub,key=max(eligible,key=lambda e:e[0]);chosen.append(x);local[pub]+=1;global_counts[pub]+=1;seen.add(x['source_url']);titles.add(key)
        result.extend(chosen)
    return result

def main():
    now=dt.datetime.now(dt.timezone(dt.timedelta(hours=8)))
    candidates=[];errors=[];source_counts={};source_log=[]
    with cf.ThreadPoolExecutor(max_workers=20) as ex:
        futures={ex.submit(fetch,s,now):s for s in SOURCES}
        for f,s in futures.items():
            try:
                found=f.result();candidates.extend(found);source_counts[s['name']]=len(found);source_log.append(dict(name=s['name'],url=s['url'],publisher_id=s['publisher_id'],candidates=len(found),status='ok'))
            except Exception as e: source_counts[s['name']]=0;errors.append({'source':s['name'],'error':type(e).__name__});source_log.append(dict(name=s['name'],url=s['url'],publisher_id=s['publisher_id'],candidates=0,status='failed',error=type(e).__name__))
    items=select(candidates,now)
    counts={c:sum(x['category']==c for x in items) for c in TARGETS}
    chinese=sum(x.get('source_language')=='zh' for x in items)
    ratio=chinese/len(items) if items else 0
    report=dict(chinese_count=chinese,chinese_ratio=ratio,schema_version=1,date=now.date().isoformat(),collected_at=now.isoformat(),status='ready_for_publication',mode='rss_excerpt',counts=counts,shortfalls={c:n-counts[c] for c,n in TARGETS.items() if counts[c]<n},items=items,notice='RSS来源简介，保留原文语言；未经独立事实核查。')
    from collections import Counter
    selected_feeds=Counter(x.get('feed_url') for x in items)
    for entry in source_log:entry['selected']=selected_feeds[entry['url']]
    diversity={cat:dict(Counter(x['publisher_id'] for x in items if x['category']==cat)) for cat in TARGETS}
    Path('rss-run-log.json').write_text(json.dumps(dict(sources=source_log,enabled_subscriptions=len(SOURCES),enabled_publishers=len(set(x['publisher_id'] for x in SOURCES)),selected_publishers=len(set(x['publisher_id'] for x in items)),diversity=diversity,selection_shortfalls={c:TARGETS[c]-counts[c] for c in TARGETS if counts[c]<TARGETS[c]},soft_target_report={c:{'regions':dict(Counter(x.get('region','unknown') for x in items if x['category']==c)),'tech_related':sum(bool(x.get('is_tech_related')) for x in items if x['category']==c)} for c in TARGETS},source_candidates=source_counts,chinese_count=chinese,total=len(items),chinese_ratio=ratio,counts=counts,candidates=len(candidates),errors=errors),ensure_ascii=False,indent=2))
    if any(len([x for x in items if x['category']==cat])==5 and len(diversity[cat])<3 for cat in TARGETS):
        sys.exit('Publisher diversity insufficient; previous data preserved')
    if ratio<0.70:
        sys.exit(f'Chinese source share {chinese}/{len(items)} below 70%; previous website data preserved')
    if len(items)<14 or any(counts[c]<TARGETS[c]/2 for c in TARGETS):
        sys.exit('Insufficient feed coverage; previous website data preserved. See rss-run-log.json')
    p=Path('daily');p.mkdir(exist_ok=True)
    path=p/(report['date']+'.json');path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    Path('rss-report-path.txt').write_text(str(path))
    print(json.dumps(counts))
if __name__=='__main__': main()
