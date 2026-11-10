"""Notify only after the deployed news data matches this commit. Never log secrets."""
import json
import os
from pathlib import Path
import sys
import time
import urllib.parse
import urllib.request


def main():
    key = os.environ.get('SERVERCHAN_SENDKEY', '').strip()
    if not key:
        sys.exit('Missing GitHub Actions secret: SERVERCHAN_SENDKEY')
    if not key.startswith('SCT') or not key.isalnum():
        sys.exit('Expected a ServerChan Turbo SendKey starting with SCT')
    expected = Path('news-data.js').read_bytes()
    raw = expected.decode().removeprefix('window.NEWS_DATA = ').rstrip(';\n')
    data = json.loads(raw)
    if not data.get('items'):
        sys.exit('No news to notify')
    url = 'https://zky519.github.io/'
    for attempt in range(12):
        try:
            req = urllib.request.Request(url + 'news-data.js?check=' + str(time.time()), headers={'Cache-Control': 'no-cache'})
            if urllib.request.urlopen(req, timeout=20).read() == expected:
                break
        except Exception:
            pass
        if attempt == 11:
            sys.exit('Live news does not match this deployment; notification cancelled')
        time.sleep(10)
    body = urllib.parse.urlencode({
        'title': '每日新闻已更新',
        'desp': f"每日新闻已更新，本期共 {len(data['items'])} 条。\n\n[点击打开新闻工作台]({url})\n\n{url}",
    }).encode()
    try:
        request = urllib.request.Request('https://sctapi.ftqq.com/' + key + '.send', data=body, method='POST')
        result = json.loads(urllib.request.urlopen(request, timeout=30).read())
    except Exception:
        sys.exit('ServerChan request failed; inspect provider delivery history before retrying')
    if result.get('code') != 0:
        sys.exit('ServerChan rejected notification; check account/channel settings')
    print('ServerChan accepted the news update notification')


if __name__ == '__main__':
    main()
