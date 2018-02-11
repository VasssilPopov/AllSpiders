# -*- coding: utf-8 -*-
import scrapy
import logging
import json
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
from urllib2 import quote

# scrapy runspider PIKSpider.py -o Reports/PIK-2017-05-17.json -t jsonlines
# RunIt 2017-05-17

'Get the yesterday date'
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
urlDate=yesterday.strftime("%d-%m-%Y")



class PIKSpider(scrapy.Spider):
    name = "PIK"
    allowed_domains = ['pik.bg']
    start_urls = ["http://pik.bg/novini-za-"+urlDate+".html"]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
	
    def __init__(self):
		# "Empty output file"
        fileName="PIK/Reports/PIK-%s.json"%(Yesterday)
        f = open(fileName, 'w').close()
        print '-'*10,'PIK v(1.0)','-'*10

 
    def parse(self, response):
        print 'Page: %s' % response.url
        self.links=response.xpath('//div[@class="right_part"]/a/@href').extract()
        'take only the end of the PIK url. The number after the news string:'
        # self.links_seen = map(lambda url: url.split('news')[1] , self.links_seen)
        self.links = map(lambda url: url.split('news')[1] , self.links)

        # urls = response.css('div.quote > span > a::attr(href)').extract()
        # urls = response.xpath('//div[@class="right_part"]/a/@href').extract()
        urls = response.xpath('//a[contains(@class, "img-wrap") and contains(@class, "left")]/@href').extract()
        print "url: %s selected: %d" %(response.url, len(urls))
        for url in urls:
            # if (url.split('news'))[1] not in self.links_seen:
            # url = response.urljoin(url)
            print url[-11:]
            yield scrapy.Request(url=url, callback=self.parse_details)
        
        # follow pagination link
        # next_page_url = response.css('li.next > a::attr(href)').extract_first()
        # next_page_url = response.xpath('//div[@id="content"]/div[@class="pagination_wrap"]/a[@class="next_page"]/@href').extract_first()
        next_page_url = response.xpath('//a[@class="next_page"]/@href').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        
    def parse_details(self, response):
        url   = response.url
        # title = response.xpath('//*[@id="hdscrolll"]/div/text()').extract_first()
        title = response.xpath('//h2[@class="news-title left w100"]/text()').extract_first()

        if url.split('news')[0] in ['http://pik.bg/-', 'http://pik.bg/--']:
            print url
            return
        
        art_alternatives = {}
        art_alternatives[0] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div[@class="page-header"]/p/text()').extract()
        art_alternatives[1] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/text()|//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/a/span/strong/text()').extract()
        art_alternatives[2] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/span/text()').extract()
        art_alternatives[3] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div[@class="lead"]/p/text()').extract()
        art_alternatives[4] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div/p/text()|//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div/p/strong/text()').extract()
        art_alternatives[5] = response.xpath('//*[@id="id_591b40067b1098c59050244"]/p/text()').extract()
        art_alternatives[6] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div/div[@class="text-wrapper"]/div[@class="article-text-inner-wrapper"]/p/text()').extract()
        art_alternatives[7] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div/div[@class="text-wrapper"]/div[@class="article-text-inner-wrapper"]/p/text()').extract()
        art_alternatives[8] = response.xpath('//div[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div[@class="page-header"]/text()').extract()
        art_alternatives[9] = response.xpath('//div[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div/text()').extract()
        art_alternatives[10] = response.xpath('//div[@id="news-body"]/div/div[@class="field-items"]/div[@class="field-item even"]/p/text()').extract()
        art_alternatives[11] = response.xpath('//div[@class="content_box"]/div[@class="text"]/p/text()').extract()
        art_alternatives[12] = response.xpath('//div[@class="text2"]/p/span/span/text()').extract()
        
        art_alternatives[13] = response.xpath('//div[@id="content"]/div/div/div/div/div/div/p/text()').extract()
        art_alternatives[14] = response.xpath('//div[@id="content"]/div/div/div/div/div/div/div/div[@class="_d97"]/text()').extract()
        art_alternatives[15] = response.xpath('//div[@id="content"]/div/div/div/div/p/text()').extract()
        art_alternatives[16] = response.xpath('//div[@class="news-detail left w100"]/p/text()').extract()
        art_alternatives[17] = response.xpath('//div[@class="news-detail left w100"]/p/span/text()').extract()
        art_alternatives[18] = response.xpath('//div[@id="articlebody"]/text() | //div[@id="articlebody"]/p/text() | //div[@id="anons"]/text()').extract()
        art_alternatives[19] = response.xpath('//div[@class="news-detail left w100"]/div/text() | //div[@class="news-detail left w100"]/div/div/text()').extract()
        
        for key in art_alternatives:
            art_alternatives[key] = list( map   ( lambda str: str.strip(), art_alternatives[key] ) )
            art_alternatives[key] = list( filter( lambda str: str != u'' , art_alternatives[key] ) )
            art_alternatives[key] = ' '.join(art_alternatives[key])

        art_alternatives = list( filter( lambda str: str != u'' , art_alternatives.values() ) )	

        article=u' '.join(art_alternatives)
        # print article
        # (day,month,year) = response.css('time.left::text').extract()[0].split('|')[1].split('.')
        # time = year+"."+month+"."+day.strip()
        # pubTime=response.xpath('//div[@class="left info"]/div[@class ="left info_left"]/div[@class="left clock"]/time[@class="left text"]/text()').extract_first()
        # (day,month,year) = pubTime.split('|')[1].strip().split('.')
        # pubDate='%s.%s.%s'%(year,month,day)
        pubTime=response.xpath('//span[@class="txt left"]/text()').extract_first()
        (day,month,year) = pubTime.split('.')
        pubDate='%s.%s.%s'%(year,month,day)
        
        yield {
            'url': url,
            'title': title,
            'text': article,
            'date': pubDate

        }	