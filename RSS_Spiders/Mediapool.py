# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class MediapoolSpider(XMLFeedSpider):
    name = 'Mediapool'
    allowed_domains = ['www.mediapool.bg/rss']
    start_urls = ['http://www.mediapool.bg/rss/feed.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        i['url'] = selector.select('link').extract()
        i['name'] = selector.select('title').extract()
        i['description'] = selector.select('description').extract()
        return i
