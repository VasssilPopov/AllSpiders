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

def getStdDate(dateString):

    months ={u'ян.':'01', u'февр.':'02', u'март':'03', u'апр.':'04', u'май':'05', u'юни':'06',
          u'юли':'07', u'авг.':'08', u'септ.':'09', u'окт.':'10', u'ноем.':'11', u'дек.':'12'}

    (day,month, year)=dateString.split('|')[1].strip() .split(' ')
    dateExpr='????.??.??'

    if (month in months):
        month = months[month]
        dateExpr =  '%s.%s.%s' % (year, month, ('00'+day)[-2:])

    return dateExpr    

class EpicenterSpider(scrapy.Spider):
    name = 'epicenter'
    allowed_domains = ['epicenter.bg']
    start_urls = [
        'http://epicenter.bg/category/bulgaria/2',
        'http://epicenter.bg/category/law/3',
        'http://epicenter.bg/category/business/4',
        'http://epicenter.bg/category/obstestvo/11',
        'http://epicenter.bg/category/culture/6',
        'http://epicenter.bg/category/world/7',
        'http://epicenter.bg/category/sport/8',
        'http://epicenter.bg/category/weekend/10',
        'http://epicenter.bg/category/recipes/9',
        ]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'CONCURRENT_REQUESTS_PER_DOMAIN': '1',
        'DOWNLOAD_DELAY': '2',
        'COOKIES_ENABLED': 'False',
        'DEPTH_LIMIT':'4'
        }


    def __init__(self):

        print '__init__'
        
        self.json_datafile = 'Epicenter/Reports/Epicenter-' + Today + '.json'
        self.links_seen = read_ids(self.json_datafile)
        
        self.links_seen = set(map(lambda url: url.split('/')[-3],
                              self.links_seen))
                              
        print '-' * 10, 'Epicenter v(1.0)', '-' * 10
        # print self.links_seen
        print 'seen: %d' % len(self.links_seen)


    def parse(self, response):
    
        print '<parse> url:', response.url
        
        # urls = response.xpath('//a[@class="catItemTitle"]/@href').extract()
        urls = response.xpath('//tr/td[@class="products_list"]/a/@href').extract()
        print len(urls)
        for url in urls:
            code=url.split('/')[-3]
            print code, code not in self.links_seen
            if code not in self.links_seen:
                self.links_seen.add(code)

            url = response.urljoin(url)
            # check is url saved if not 
            yield scrapy.Request(url=url, callback=self.parse_details)

            # follow pagination link

        # # next_page_url=response.xpath('//li/a[@class="pagenav"]/@href').extract()
        # next_page_url=response.xpath('//div[@class="pagination"]/a[last()]/@href').extract_first()
        # if ('date?start=' in next_page_url[-2]):
            # next_page_url = response.urljoin(next_page_url[-2])
            # print 'NEXT PAGE url: %s' % next_page_url
            # yield scrapy.Request(url=next_page_url,
                    # callback=self.parse)

    def parse_details(self, response):

        print 'parse_details'

        url = response.url
        
        title=response.xpath('//tr/td/h1/text()').extract_first()
        
        texts=response.xpath('//div[@id="adjuster"]/p/text()').extract()
        article=u' '.join(texts)
        
        pubDate=response.xpath('//tr/td/div/p[@class="tinytext-novina"]/text()').extract_first()
        articleDate = getStdDate(pubDate)

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
