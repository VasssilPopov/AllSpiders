# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class ClubzSpider(XMLFeedSpider):
    name = 'ClubZ'
    allowed_domains = ['www.clubz.bg/rss.xml']
    start_urls = ['http://www.clubz.bg/rss.xml/feed.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        i = {}
        i['link'] = selector.select('link').extract()
        i['title'] = selector.select('title').extract()
        i['description'] = selector.select('description').extract()
        return i
