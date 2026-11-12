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
if __name__=='__main__':unittest.main()
