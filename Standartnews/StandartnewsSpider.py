# -*- coding: utf-8 -*-
import scrapy
import logging
from datetime import date, timedelta
# import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
# cd _AllSpiders
# Python RunClubZSpider.py

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
import logging

'Get the yesterday date'
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y.%m.%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%Y.%m.%d").lower()
logger = logging.getLogger('myLogger')

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
	
class StandartNewsSpider(scrapy.Spider):
    name = "StandartNews"
    # allowed_domains = ['http://standartnews.com']
    start_urls = [
        # 'http://standartnews.com/biznes.html', 
        # 'http://standartnews.com/svyat.html', 
        # 'http://standartnews.com/balgariya.html'
        'http://standartnews.com/balgariya.html', 
        'http://standartnews.com/biznes.html', 
        'http://standartnews.com/svyat.html', 
        'http://standartnews.com/mneniya.html', 
        'http://standartnews.com/kultura.html', 
        'http://standartnews.com/sport.html', 
        'http://standartnews.com/lyubopitno.html', 
        'http://standartnews.com/regionalni.html', 
            ]
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    pubDate = ''
    def __init__(self):
        self.json_datafile = 'StandartNews/Reports/StandartNews-'+Today+'.json'
        self.links_seen = read_ids(self.json_datafile)
        'take only the end of the StandartNews url. The number after the news string:'
        # self.links_seen = map(lambda url: url.split('news')[1] , self.links_seen)
        print '-'*10,'StandartNews v(1.0)','-'*10

    def parse(self, response):

        print 'parse URL: %s' % (response.url)
        # links=response.xpath('//div[@class="single_news_list_small"]')

        links=response.xpath('//div[@class="single_news_list_small"]/div[@class="news_content_list"]')

        # print "Selected: %d" %(len(links))
        
        for cnt, link in enumerate(links, 1):
            # process date 
            dateInfo = link.xpath('.//comment()').extract_first()
            
            (day, month, year)=dateInfo.split('|')[1].strip().split('.')
            pubDate='%s.%s.%s' % (year, month, day)

            if (pubDate == strToday):
                # print cnt, 'Today'
                continue
                
            if (pubDate != Yesterday):
                return
            # print cnt, '>> >Yesterday'
            url = link.xpath('.//h2/a[@class="title_news_list"]/@href').extract_first()
            
            # print cnt,'\t', pubDate, strToday,url
            if url not in self.links_seen:
                # add an url into self.links_seen
                self.links_seen.add(url)
                url = response.urljoin(url)
                #print '@d\tPubDate: %s Today: %s Url: %s' %(cnt, pubDate, strToday, url)
                # print '>1>',url
                yield scrapy.Request(url=url, callback=self.parse_details, meta={'pubDate': pubDate})

        # follow pagination link
        next_page_url=response.xpath('//tr/td/a[@rel="next"]/@href').extract_first()
        # print 'next_page_url: %s' % (next_page_url)
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            print 'next_page_url: %s' % (next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
            # yield scrapy.Request(url=next_page_url, callback=self.parse, errback=self.errback_httpbin,
            #                        dont_filter=True)

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)            
                
                
            
    def parse_details(self, response):
        
        # print 'parse_details'
        url     = response.url
        
        pageTitle=response.xpath('//div[@id="articleContentHolder"]/div/h2/text()').extract_first().strip()
        
        texts=response.xpath('//div[@id="articleContentHolder"]/div/div/div["articlBodyHolder"]/p/text()').extract()
        pageText=u' '.join(texts)
        pageDate=response.meta['pubDate']
        
        # print 'pageDate: %s url= %s ' %(pageDate, url)
        # Filter on todays date
        # 
        # print pageDate, strToday,(pageDate == strToday), url
        # if (pageDate == strToday):
        yield {
            'url': url,
            'title': pageTitle,
            'text': pageText,
            'date': pageDate
        }

