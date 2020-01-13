# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import date, timedelta
from sys import exit, path
import platform

if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

from Dates import *
import os.path


yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
	
class DnevnikSpider(scrapy.Spider):
    name = "Dnevnik"
    # start_urls = ["http://m.dnevnik.bg/allnews/"+yesterday.strftime("%Y/%m/%d")]
    start_urls = ["http://dnevnik.bg/allnews/yesterday/"]
    # start_urls = ["http://dnevnik.bg/allnews/2017/07/29/"]
    count = 0
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'DOWNLOAD_DELAY':'2',
        'COOKIES_ENABLED':'False',
        'CONCURRENT_REQUESTS_PER_DOMAIN':'1',
    }	
    def __init__(self):
        # "Empty output file"
        fileName="Dnevnik/Reports/Dnevnik-%s.json"%(Yesterday)
        f = open(fileName, 'w').close()
        print '-'*10,'Dnevnik v(1.0)','-'*10
    def parse(self, response):

        urls=response.xpath('//article[@class="secondary-article-v2 border-top list-item"]/div[@class="text"]/h2/a/@href').extract()
        print "url: %s selected: %d" %(response.url, len(urls))

        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_page)
        
    def parse_page(self, response):
        url = response.url

        title = response.xpath('//div[@class="content"]/h1/text() | //aside/div[@class="module"]/div[@class="site-block"]/div[@class="the-picture-summary article"]/h2/text()').extract_first()
        if title is None:
            title=''
        article=u' '.join(response.xpath('//div[@class="article-content"]/p/text()| //div[@class="article-content"]/h2/text() | //div[@class="article-content"]/p/a/text()| //div[@class="article-content"]/div[@class="story"]/p/text() | //div[@class="article-content"]/div[@class="story"]/text() | //div[@class="module"]/div[@class="site-block"] /div[@class="the-picture-summary article"]/p/text()').extract())
        # 'extract and prepare Article date'
        pubDate = response.xpath('//div[@class="article-tools"]/time/text()').extract_first()

        articleDate = dcDnevnik(pubDate)
        
        yesterdaysDate=yesterday.strftime("%Y.%m.%d")
        self.count = self.count + 1
        # Filter on todays date
        print '>>> ', ++(self.count), articleDate, yesterdaysDate
        if ((articleDate == yesterdaysDate) and ( len(article)) > 0):
            yield {
                'url': url,
                'title': title,
                'text': article,
                'date': articleDate
            }	
        else:
            pass