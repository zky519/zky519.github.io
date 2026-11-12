import json
from pathlib import Path
p=Path('news-data.js')
data=json.loads(p.read_text().removeprefix('window.NEWS_DATA = ').rstrip(';\n'))
data['notice']='本期 '+str(len(data['items']))+' 条'
for x in data['items']:
    x['verification']='rss_source_excerpt'
    x['context']=''
p.write_text('window.NEWS_DATA = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
