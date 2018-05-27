# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import date, timedelta
import os.path

import jsonlines
import json

yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
yesterdaysDate = yesterday.strftime("%Y.%m.%d")
BGMonths={u'януари':'01',u'февруари':'02',u'март':'03',u'април':'04',u'май':'05',u'юни':'06',u'юли':'07',u'август':'08',u'септември':'09',u'октомври':'10',u'ноември':'11',u'декември':'12'}
removeFile = 1

class CrossSpider(scrapy.Spider):
    name = "cross"
    start_urls=[
    'http://www.cross.bg/archive/yesterday',
    ]
    count = 0
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
        }
    def __init__(self):
        print '-'*10,'Cross v(1.0)','-'*10
        
        # zeroes the file
        fileName="Cross/Reports/Cross-%s.json"%(Yesterday)
        if (os.path.exists(fileName) and os.path.getsize(fileName) > 0):
                f = open(fileName, 'w').close()

    def parse(self, response):
    
        print 'Page url %s' % (response.url)

        urls=response.xpath('//ul[@class="newsList"]/li/div[@class="articleDetiles"]/a[@class="nTitle"]/@href').extract()
        print len(urls),' urls collected'
        for url in urls:
            #url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_page)
        
        next_page_url = response.xpath('//div[@class="pagging"]/a[@class="nextPage"]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        
    def parse_page(self, response):
        url = response.url

        title=response.xpath('//div[@class="articleWraper"]/h1[@class="articleTitle"]/text()').extract_first()

        pageTexts = response.xpath('//div[@class="articleWraper"]/div[@class="rightPart"]/p/text()').extract()
        article=u' '.join(pageTexts)

        texts = response.xpath('//div[@class="articleWraper"]/div[@class="rightPart"]/p/text() | //div[@class="articleWraper"]/div[@class="rightPart"]/p/span/text()').extract()
        article=u''.join(texts)
        # 'extract and prepare Article date'
        # pageDate = response.xpath('//div[@class="articleWraper"]/div[@class="articleInfo"]/p[@class="fl"]/text()').extract_first()
        # (day, month, year)=pageDate.split('|')[0].split()
        # articleDate = '%s.%s.%s' % (year,BGMonths[month.lower()],day)
        aDate = response.xpath('//div[@class="articleInfo"]/p[@class="fl"]/text()').extract_first()
        (day, month, year)=aDate.split('|')[-2].strip().split()
        articleDate='%s.%s.%s' % (year, BGMonths[month.lower()], day)
        
        # data=response.xpath('//div[@class="newsdate"]/span/text()').extract_first()
        # (day, month, year)=data.split(',')[0].split()
        # articleDate = '%s.%s.%s' % (year,BGMonths[month],day)
        
        self.count = self.count + 1
        print '\t', self.count, articleDate,(articleDate == yesterdaysDate),url
        # Filter on todays date
        if (articleDate == yesterdaysDate):
            yield {
                'url': url,
                'title': title,
                'text': article,
                'date': articleDate
            }    
