# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class SegabgSpider(XMLFeedSpider):
    name = 'SegaBG'
    allowed_domains = ['www.segabg.com/rss20.xml']
    start_urls = ['http://www.segabg.com/rss20.xml/feed.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        i['url'] = selector.select('link').extract()
        i['name'] = selector.select('title').extract()
        i['description'] = selector.select('description').extract()
        return i
