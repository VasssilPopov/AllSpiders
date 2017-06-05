# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class SegabgSpider(XMLFeedSpider):
    name = 'SegaBG'
    allowed_domains = ['www.segabg.com/rss20.xml']
    start_urls = ['http://www.segabg.com/rss20.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        i['url'] = selector.select('link').extract()
        i['title'] = selector.select('title').extract()
        i['text'] = selector.select('description').extract()
		i['date'] = '-'.join(selector.select('pubDate').split()[1:4])
		# test
		return i
