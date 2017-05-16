# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class PikSpider(XMLFeedSpider):
    name = 'PIK'
    allowed_domains = ['pik.bg/rss/index/2']
    start_urls = ['http://pik.bg/rss/index/2/feed.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        i['url'] = selector.select('link').extract()
        i['name'] = selector.select('title').extract()
        i['description'] = selector.select('description').extract()
        return i
