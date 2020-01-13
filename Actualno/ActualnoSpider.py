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
import jsonlines


yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
yesterdaysDate = yesterday.strftime("%Y.%m.%d")
BGMonths={u'януари':'01',u'февруари':'02',u'март':'03',u'април':'04',u'май':'05',u'юни':'06',u'юли':'07',u'август':'08',u'септември':'09',u'октомври':'10',u'ноември':'11',u'декември':'12'}

class ActualnoSpider(scrapy.Spider):
    name = "Actualno"
    start_urls=[
    'https://www.actualno.com/yesterday',
    ]
    count = 0
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
        }
    def __init__(self):
        print '-'*10,'Actualno v(1.0)','-'*10
        
        # zeroes the file
        fileName="Actualno/Reports/Actualno-%s.json"%(Yesterday)
        if (os.path.exists(fileName) and os.path.getsize(fileName) > 0):
                f = open(fileName, 'w').close()

    def parse(self, response):
    
        print 'Page url %s' % (response.url)
        
        # # zeroes the file
        # fileName="Actualno/Reports/Actualno-%s.json"%(Yesterday)
        # if (os.path.exists(fileName) and os.path.getsize(fileName) > 0):
            # f = open(fileName, 'w').close()

        # urls=response.xpath('//article[@class="secondary-article-v2 border-top list-item"]/div[@class="text"]/h2/a/@href').extract()
        urls=response.xpath('//div[@class="info"]/a[@class="title"]/@href').extract()
        print len(urls),' urls collected'
        for url in urls:
            # url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_page)
        
        if (response.xpath('//div[@class="pagginator"]/a[last()]/text()').extract_first()[-2:] == '>>'):
            next_page_url=response.xpath('//div[@class="pagginator"]/a[last()]/@href').extract_first()
            next_page_url=response.urljoin(next_page_url)
            print 'will follow next page: %s' % (next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        # next_page_url=response.xpath('//div[@class="pagginator"]/a/@href').extract()[3]
        # if next_page_url:
            # next_page_url=response.urljoin(next_page_url)
            # print 'will follow next page: %s' % (next_page_url)
            # yield scrapy.Request(url=next_page_url, callback=self.parse)
            
    def parse_page(self, response):

        url = response.url

        title=response.xpath('//article[@id="article-content"]/h1/text() | //article[@id="article-content"]/h1/b/text()').extract_first()
        
#        texts=response.xpath('//div[@id="main_container"]/div/div/text() | //div[@id="main_container"]/div/div/text()').extract()
        texts=response.xpath('//div[@id="main_container"]/div/div/text() | //div[@id="main_container"]/div/p/text() | //div[@id="main_container"]/div/p/b/text() | //div[@id="main_container"]/div/div/i/text()| //div[@id="content_inner_article_box"]/div/div/b/text()| //div[@id="content_inner_article_box"]/div/div/text()').extract()
        l = list()
        for text in texts:
            l.append(text.strip())
        article=u' '.join(l)

        # 'extract and prepare Article date'
        time=response.xpath('//div[@class="info"]/time/text()').extract_first().strip()
        (day, month,year)=time.split()[0].split('.')
        
        articleDate = '%s.%s.%s' % (year,month,day)
        
        self.count = self.count + 1
        print self.count,'\t', articleDate,(articleDate == yesterdaysDate), url
        # Filter on todays date
        if (articleDate == yesterdaysDate):
            yield {
                'url': url,
                'title': title, 
                'text': article,
                'date': articleDate
            }    
