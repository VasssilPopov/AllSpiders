from scrapy.spiders import XMLFeedSpider
from items import TestItem

class MySpider(XMLFeedSpider):
    name = 'http://standartnews.com'
    allowed_domains = ['http://standartnews.com']
    start_urls = ['http://standartnews.com/rss.php?c=1',
    'http://standartnews.com/rss.php?c=2',
    'http://standartnews.com/rss.php?c=137',
    'http://standartnews.com/rss.php?c=115',
    'http://standartnews.com/rss.php?c=117',
    'http://standartnews.com/rss.php?c=118',
    'http://standartnews.com/rss.php?c=135',
    ]
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'DOWNLOAD_DELAY':'5',
        'COOKIES_ENABLED':'False',
	}

    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))

        item = TestItem()
        item['url'] = node.xpath('//link/text()').extract()
        item['title'] = node.xpath('//title/text()').extract()[1]
        item['text'] = node.xpath('//description/text()').extract()
        item['date'] = node.xpath('//pubDate/text()').extract()
        return item
