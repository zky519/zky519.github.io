import datetime as dt
import unittest
from collect_rss import parse_feed,select
class Tests(unittest.TestCase):
    def test_filter_and_html(self):
        raw=b'<rss><channel><item><title>AI news</title><link>https://example.com/a</link><pubDate>Thu, 12 Nov 2026 00:00:00 GMT</pubDate><description>&lt;p&gt;Actual excerpt&lt;/p&gt;</description></item><item><title>AI future</title><link>https://example.com/b</link><pubDate>Fri, 13 Nov 2026 00:00:00 GMT</pubDate></item></channel></rss>'
        now=dt.datetime(2026,11,12,1,tzinfo=dt.timezone.utc)
        items=parse_feed(raw,('test','https://example.com','ai','china'),now)
        self.assertEqual(len(items),1);self.assertEqual(items[0]['summary'],'Actual excerpt')
        self.assertEqual(len(select(items+items,now)),1)
    def test_chinese_games_and_language(self):
        now=dt.datetime(2026,11,16,2,tzinfo=dt.timezone.utc)
        def feed(title):
            return ('<rss><channel><item><title>'+title+'</title><link>https://example.com/a</link><pubDate>Mon, 16 Nov 2026 00:00:00 GMT</pubDate></item></channel></rss>').encode()
        source=('机核','https://www.gcores.com/rss','games','international')
        items=parse_feed(feed('《塞尔达传说》重制版正式公布'),source,now)
        self.assertEqual(items[0]['source_language'],'zh')
        self.assertEqual(items[0]['region'],'international')
        self.assertEqual(parse_feed(feed('游戏改编电影正式上映'),source,now),[])
        self.assertEqual(len(parse_feed(feed('F1大奖赛汉密尔顿赛后采访'),('test','https://example.com','f1','international'),now)),1)
    def test_chinese_priority(self):
        now=dt.datetime(2026,11,16,2,tzinfo=dt.timezone.utc)
        items=[dict(title=str(i),source_url='https://example.com/'+str(i),category='ai',region='international',source_language='zh' if i<5 else 'en',published_at=now.isoformat()) for i in range(9)]
        self.assertTrue(all(x['source_language']=='zh' for x in select(items,now)))
    def test_publisher_caps_and_language(self):
        from collections import Counter
        now=dt.datetime(2026,11,16,2,tzinfo=dt.timezone.utc)
        candidates=[]
        for cat in ('ai','politics_economy','games','f1'):
            for pub in range(8):
                for n in range(8):
                    candidates.append(dict(title=f'{cat}-{pub}-{n}',source_url=f'https://p{pub}.example/{cat}/{n}',publisher_id=f'p{pub}',category=cat,region='international',source_language='zh' if pub<6 else 'en',published_at=now.isoformat()))
        selected=select(candidates,now)
        self.assertEqual(len(selected),17)
        self.assertGreaterEqual(sum(x['source_language']=='zh' for x in selected)/17,0.7)
        self.assertLessEqual(max(Counter(x['publisher_id'] for x in selected).values()),3)
        for cat in ('ai','politics_economy','games'):
            counts=Counter(x['publisher_id'] for x in selected if x['category']==cat)
            self.assertGreaterEqual(len(counts),3);self.assertLessEqual(max(counts.values()),2)
    def test_bbc_channels_share_cap(self):
        now=dt.datetime(2026,11,16,2,tzinfo=dt.timezone.utc)
        items=[dict(title=str(n),source_url=f'https://bbc.example/{n}',publisher_id='bbc',category='politics_economy',region='international',source_language='zh',published_at=now.isoformat()) for n in range(20)]
        self.assertEqual(len(select(items,now)),2)
        for x in items:x['published_at']=(now-dt.timedelta(hours=73)).isoformat()
        self.assertEqual(select(items,now),[])
if __name__=='__main__':unittest.main()
