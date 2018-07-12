# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
import os
import json
import json_lines
from scrapy.exceptions import CloseSpider
from scrapy.spiders import Rule
from sys import exit, path
import platform
if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

'Prepare standart set of dates (Yesterday, Today, strToday)'
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y.%m.%d")
dateYesterday= yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%d %b %Y").lower()

class BgOnAirSpider(scrapy.Spider):

    name = "BgOnAir"
    start_urls = ['https://www.bgonair.bg/listing/bulgaria',
                  'https://www.bgonair.bg/listing/economy',
                  'https://www.bgonair.bg/listing/world',
                  'https://www.bgonair.bg/listing/science',
                  ]
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
    #		'DOWNLOAD_DELAY':'5',
        'COOKIES_ENABLED':'False',
    }

    def __init__(self):
        # "Empty output report file."
        fileName="BgOnAir/Reports/BgOnAir-%s.json"%(yesterday.strftime("%Y-%m-%d"))
        f = open(fileName, 'w').close()
        
        print '-'*10,'BgOnAir v(1.0)','-'*10

    def nextPage(self, next_page):
        if next_page == '':
            return 'page=2'
        else:
            ind=int(next_page.split('=')[1])
            return 'page='+str(ind+1)

    def nextPageUrl(self, npUrl):
        if npUrl.find('?')>-1:
            return npUrl.split('?')[0]+'?'+nextPage(npUrl.split('?')[1])
        else:
            return npUrl.split('?')[0]+'?page=2'

    def parse(self, response):
        print '---->',response.url
        urls=response.xpath('//div[@class="row"]/div[@class="caption"]/a/@href').extract()
        for url in urls:
            pubDate= url.split("/")[-2]
            print 'pubDate:'+pubDate
            if pubDate > dateYesterday:
                print '>>> Skipped: ',url
                pass
            elif pubDate == dateYesterday:
                print '>>> Selected: ',url
                yield scrapy.Request(url=url, callback=self.parse_details)
            else:
                print '>>> Stopped: ',url
                return

        # follow pagination link
        #next_page_url=response.xpath('//div[@class="row article-list"]/div[@class="list-pager row"]/div/a[@class="arrow right isprite"]/@href').extract_first()
        next_page_url = self.nextPageUrl(response.url)
        print '>>1>> next_page_url: %s' % (next_page_url)
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
            
    def parse_details(self, response):
        
        print '>>> parse details'
        url = response.url
        
        pageTitle = response.xpath('//div[@class="row Article"]/div[@class="item"]/div[@class="row"]/div/h1[@class="h1_title"]/text()').extract_first()
        
        pageTexts = response.xpath('//div[@id="article-detail-text"]/span/p/text() | //div[@id="article-detail-text"]/span/p/span/text() | //div[@id="article-detail-text"]/span/div/span/text()').extract()
        pageText=u' '.join(pageTexts)
        
        # pageDate = response.xpath('//div[@id="content-main"]/article[@class="article-inner"]/header/div[@class="article-info"]/p[@class="time"]/@content').extract_first()
        # pageDate=pageDate.split('T')
        # pageDate=pageDate[0].replace('-','.')
        # print pageDate,Yesterday, pageDate==Yesterday
        
        
        # if (pageDate == Yesterday):
            # print 'saved'
        yield {
            'url': url,
            'title': pageTitle,
            'text': pageText,
            'date': Yesterday
        }