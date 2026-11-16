import json,datetime as dt,urllib.request,xml.etree.ElementTree as ET,concurrent.futures as cf
from pathlib import Path
import collect_rss as old
now=dt.datetime.now(dt.timezone.utc)
def probe(s):
 try:
  req=urllib.request.Request(s['url'],headers={'User-Agent':'Mozilla/5.0 (compatible; DailyNewsRSS/2.0)'})
  with urllib.request.urlopen(req,timeout=12) as r:raw=r.read(4000001);s['final_url']=r.url
  root=ET.fromstring(raw);assert root.tag.split('}')[-1] in {'rss','feed','RDF'}
  entries=root.findall('.//item') or root.findall('.//{http://www.w3.org/2005/Atom}entry') or root.findall('.//{http://purl.org/rss/1.0/}item')
  dates=[]
  for e in entries:
   f={c.tag.split('}')[-1]:c.text or '' for c in e};d=old.parse_date(f.get('pubDate') or f.get('published') or f.get('updated') or f.get('date'))
   if d:dates.append(d)
  recent=sum(dt.timedelta(0)<=now-d<=dt.timedelta(hours=72) for d in dates)
  s.update(status='enabled' if recent else 'no_recent_content',entries=len(entries),recent_entries=recent,latest_date=max(dates).isoformat() if dates else None)
 except Exception as e:s.update(status='failed',error=type(e).__name__)
 s['checked_at']=now.isoformat();return s

if __name__=='__main__':
    p=Path('config/rss-sources.json')
    sources=json.loads(p.read_text())
    candidates=[x for x in sources if x['status']!='out_of_scope']
    with cf.ThreadPoolExecutor(max_workers=20) as ex: results=list(ex.map(probe,candidates))
    results += [x for x in sources if x['status']=='out_of_scope']
    seen=set()
    for x in results:
        if x['status']=='enabled':
            if x['final_url'] in seen:x['status']='duplicate_redirect'
            else:seen.add(x['final_url'])
    p.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
