"""Import a news-agent JSON report: python3 scripts/import_news.py /absolute/report.json"""
import json, sys
from pathlib import Path
report = json.loads(Path(sys.argv[1]).read_text())
labels = {'ai':'AI行业','politics_economy':'政治经济','games':'单机游戏','f1':'F1'}
accepted = {'official', 'reported', 'official_background', 'verified'}
items = []
for n in report['items']:
    if not (report.get('status') in {'ready_for_publication', 'partial_ready_for_publication'} and n.get('ready_for_publication') is True) and n.get('verification') not in accepted:
        continue
    items.append(dict(title=n['title'], summary=n.get('summary',''), category=labels.get(n['category'],n['category']), source=n.get('source_name',''), url=n['source_url'], publishedAt=n.get('published_at',''), context=n.get('why_it_matters',''), verification=n['verification']))
if not items:
    raise SystemExit('No publishable items; keeping previous data')
data = dict(updatedAt=report['collected_at'], reportDate=report.get('date'), items=items, revision=report.get('revision', 1), notice=f"本期 {len(items)} 条 · 新闻由采集模块核实与编辑 · 游戏保留发售计划口径，赛事保留回顾日期。")
root=Path(__file__).resolve().parent.parent
(root/'news-data.js').write_text('window.NEWS_DATA = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
if report.get('shortfalls'):
    data['notice'] = f"本期采集不完整：仅发布 {len(items)} 条；缺少" + '、'.join(f"{labels.get(k,k)} {v} 条" for k,v in report['shortfalls'].items() if v)
    (root/'news-data.js').write_text('window.NEWS_DATA = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
print(data['notice'])
