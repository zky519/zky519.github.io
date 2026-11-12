import json
from pathlib import Path
p=Path('news-data.js')
data=json.loads(p.read_text().removeprefix('window.NEWS_DATA = ').rstrip(';\n'))
data['notice']='RSS 来源简介 · 保留原文语言 · 未经独立事实核查 · 本期 '+str(len(data['items']))+' 条'
for x in data['items']:
    x['verification']='rss_source_excerpt'
    x['context']='来源自带简介，不含AI生成摘要或独立事实核查。'
p.write_text('window.NEWS_DATA = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
