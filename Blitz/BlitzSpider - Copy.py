# -*- coding: utf-8 -*-
import scrapy
import logging
import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
from sys import exit, path
from datetime import date, timedelta
import platform

if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

from ScrapingHelpers import *
from Dates import *
from urllib2 import quote

'Get the yesterday date'
# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%Y.%m.%d").lower()

def read_ids(file):

    'Read latest 11 chars from urls of the already processed publications '
    ids=set()

    try:
        with open(file, 'rb') as f:
            for item in json_lines.reader(f):
                ids.add(item["url"])
    except IOError:
        ids = set()
	# print 'error'

    return ids

class BlitzSpider(scrapy.Spider):
    name = "Blitz"
    allowed_domains = ['blitz.bg']
    start_urls = [
        "https://www.blitz.bg/svyat",
        "https://www.blitz.bg/politika",
        "https://www.blitz.bg/obshtestvo",
        "https://www.blitz.bg/ikonomika",
        "https://www.blitz.bg/kriminalni",
        "https://www.blitz.bg/intsidenti",
        "https://www.blitz.bg/zdrave",
        "https://www.blitz.bg/lyubopitno",
        "https://www.blitz.bg/layfstayl"
        
    ]
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'DOWNLOAD_DELAY':'5',
        'COOKIES_ENABLED':'False',
        # 'CONCURRENT_REQUESTS_PER_DOMAIN':'1',
    }

    def __init__(self):
        self.json_datafile = 'Blitz/Reports/Blitz-'+Today+'.json'
        self.links_seen = read_ids(self.json_datafile)
        'take only the end of the Mediapool url. The number after the news string:'
        self.links_seen = map(lambda url: url.split('news')[1] , self.links_seen)
        print '-'*10,'Blitz v(1.0)','-'*10

    def parse(self, response):

        urls=response.xpath('//article[@class="simple-post simple-big clearfix"]/a/@href | //header[@class="news-details"]/h3[@class="news-title"]/a/@href').extract()
        print "url: %s selected: %d" %(response.url, len(urls))
        for url in urls:
            if url.split('news')[1] not in self.links_seen:
                url = response.urljoin(url)
                yield scrapy.Request(url=url, callback=self.parse_details)

        # follow pagination link
        next_page_url=response.xpath('//div[@class="row pagination"]/div[2]/a[@class="btn next pull-right"]/@href').extract_first()
        if next_page_url:
            if (next_page_url[-1:]=='6'):
                print '>1> ',next_page_url
                raise CloseSpider('Index date changed')

            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):

        url     = response.url
        
        title   = response.xpath('//header/h1[@class="post-title"]/text()').extract()[0].strip()

        introStr = response.xpath('//div[@class="intro"]/text()').extract()[0].strip()
        texts= ' '.join(response.xpath('//div[@id="articleContent"]/strong/text() | //div[@id="articleContent"]/text()| //div[@id="articleContent"]/p/strong/text()| //div[@id="articleContent"]/p/text()').extract())
        article = introStr + texts

        pubDate=response.xpath('//*[@id="page-container"]/div[1]/div/div/article/header/div/ul/li[2]/text()').extract_first()
        pubDate = dcBlitz(pubDate)
        #pubDate = convertDate(pubDate)
        # print '>>', pubDate, strToday
        # articleDate=translateDateBG_EN(pubDate.split(',')[0])
        # print 'artDate: %s url= %s ' %(articleDate, url)
        # Filter on todays date
        print pubDate, strToday,(pubDate == strToday)
        if (pubDate == strToday):
            print 'saved :%s'% (url)
            yield {
                'url': url,
                'title': title,
                'text': article,
                'date': pubDate

            }
        else:
            # raise CloseSpider('Index date changed')
            pass

