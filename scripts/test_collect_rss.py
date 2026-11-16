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
if __name__=='__main__':unittest.main()
