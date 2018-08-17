#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from datetime import date, timedelta
import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
import sys

# scrapy runspider 24chasaSpider.py -o Reports/24chasa-2017-05-17.json -t jsonlines
# RunIt 2017-05-17

# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")

today = date.today()
Today = today.strftime('%Y-%m-%d')
strToday = today.strftime('%Y.%m.%d')


def read_ids(file):
    '''Read latest 11 chars from urls of the already processed publications '''

    ids = set()

    try:
        with open(file, 'rb') as f:
            for item in json_lines.reader(f):
                ids.add(item['url'])
    except IOError:
        ids = set()

    # print 'error'

    return ids


class ClassaSpider(scrapy.Spider):

    name = 'Classa'
    allowed_domains = ['classa.bg']
    start_urls = [
        'http://www.classa.bg/component/k2/itemlist/date/',
        ]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'CONCURRENT_REQUESTS_PER_DOMAIN': '1',
        'DOWNLOAD_DELAY': '2',
        'COOKIES_ENABLED': 'False',
        }

        # 'DEPTH_LIMIT':'4'

    def __init__(self):

        print '__init__'
        
        self.json_datafile = 'Classa/Reports/Classa-' + Today + '.json'
        self.links_seen = read_ids(self.json_datafile)
        self.links_seen = set(map(lambda url: url.split('/item/')[1][0:6],
                              self.links_seen))
        print '-' * 10, 'Classa v(1.0)', '-' * 10
        # print self.links_seen
        print 'seen: %d' % len(self.links_seen)


    def parse(self, response):
    
        # print '<parse> url:', response.url
        
        urls =  response.xpath('//a[@class="catItemTitle"]/@href').extract()
        for url in urls:
            code=url.split('/item/')[1][0:6]
            print code, code not in self.links_seen
            if code not in self.links_seen:
                self.links_seen.add(code)

                url = response.urljoin(url)
                # check is url saved if not 
                yield scrapy.Request(url=url, callback=self.parse_details)

            # follow pagination link

        next_page_url=response.xpath('//li/a[@class="pagenav"]/@href').extract()
        if ('date?start=' in next_page_url[-2]):
            next_page_url = response.urljoin(next_page_url[-2])
            print 'NEXT PAGE url: %s' % next_page_url
            yield scrapy.Request(url=next_page_url,
                    callback=self.parse)

    def parse_details(self, response):

        print 'parse_details'

        url = response.url
        
        title=response.xpath('//div[@class="itemHeader"]/h2[@class="itemTitle"]/text()').extract_first().strip()

        texts=response.xpath('//div[@id="k2Container"]/div/div/p/strong/span/text() | //div[@class="itemFullText"]/p/span/strong/text() | //div[@class="itemFullText"]/p/strong/span/text() | //div[@class="itemFullText"]/p/span/text() | //div[@class="itemFullText"]/div/span/text() | //div[@class="itemFullText"]/div/span/em/span/a/text() | //div[@class="itemFullText"]/h2/text() | //div[@class="itemFullText"]/p/text() | //div[@class="itemFullText"]/div[@class="article-body"]/p/span/text() | //div[@class="itemIntroText"]/p/span/text() | //div[@class="itemIntroText"]/p/span/strong/span/text() | //div[@class="itemFullText"]/div/p/span/text() | //div[@class="itemFullText"]/div/p/em/span/strong/text() | //div[@class="itemFullText"]/p/span/span/text() | //div[@class="itemFullText"]/div/ul/li/text()').extract()

        
        article=u' '.join(texts)

        pubDate=response.xpath('//div[@class="itemDateDiv"]/text()').extract_first()

        (day, month, year) = pubDate.split('.')
        articleDate = '%s.%s.%s' % (year, month, day)

        # Filter on todays date

        print '>>>>', articleDate, strToday, articleDate == strToday, url
        if articleDate == strToday:
            yield {
                'url': url,
                'title': title,
                'text': article,
                'date': articleDate,
                }
        else:
            pass
