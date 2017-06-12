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

# def fileRemove(path, fileName):

    # currentPath= os.getcwd()
    # try:
        # os.chdir(path)
        # os.remove(fileName)
    # except:
        # pass

    # os.chdir(currentPath)



class PIKSpider(scrapy.Spider):
    name = "PIK"
    # start_urls = ['http://quotes.toscrape.com']
    allowed_domains = ['pik.bg']
    start_urls = ["http://pik.bg/novini-za-"+urlDate+".html"]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
	
	
 
    def parse(self, response):
	
		# "Empty output file"
		fileName="PIK/Reports/PIK-%s.json"%(Yesterday)
		f = open(fileName, 'w').close()
	
		self.links=response.xpath('//div[@class="right_part"]/a/@href').extract()

		'take only the end of the PIK url. The number after the news string:'
		# self.links_seen = map(lambda url: url.split('news')[1] , self.links_seen)
		self.links = map(lambda url: url.split('news')[1] , self.links)

        # urls = response.css('div.quote > span > a::attr(href)').extract()
		urls = response.xpath('//div[@class="right_part"]/a/@href').extract()
		print '2. parse',len(urls)
		for url in urls:
			# if (url.split('news'))[1] not in self.links_seen:
			url = response.urljoin(url)
			yield scrapy.Request(url=url, callback=self.parse_details)
		
        # follow pagination link
        # next_page_url = response.css('li.next > a::attr(href)').extract_first()
		next_page_url = response.xpath('//div[@id="content"]/div[@class="pagination_wrap"]/a[@class="next_page"]/@href').extract_first()
		if next_page_url:
			print "next_page_url: %s"%(next_page_url)
			next_page_url = response.urljoin(next_page_url)
			yield scrapy.Request(url=next_page_url, callback=self.parse)
		
		print '------------- it is done ----------------'
    def parse_details(self, response):
		url   = response.url
		title = response.xpath('//*[@id="hdscrolll"]/div/text()').extract_first()
		

		if url.split('news')[0] == 'http://pik.bg/-':
			return
		
		art_alternatives = {}
		art_alternatives[0] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div[@class="page-header"]/p/text()')
		art_alternatives[1] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/text()|//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/a/span/strong/text()').extract()
		art_alternatives[2] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/span/text()').extract()
		art_alternatives[3] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div[@class="lead"]/p/text()').extract()
		art_alternatives[4] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div/p/text()|//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div/p/strong/text()').extract()
		art_alternatives[5] = response.xpath('//*[@id="id_591b40067b1098c59050244"]/p/text()').extract()
		art_alternatives[6] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div/div[@class="text-wrapper"]/div[@class="article-text-inner-wrapper"]/p/text()').extract()
		art_alternatives[7] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div/div[@class="text-wrapper"]/div[@class="article-text-inner-wrapper"]/p/text()').extract()
		art_alternatives[8] = response.xpath('//div[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div[@class="page-header"]/text()').extract()
		art_alternatives[9] = response.xpath('//div[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div/text()').extract()
		for key in art_alternatives:
			art_alternatives[key] = list( map   ( lambda str: str.strip(), art_alternatives[key] ) )
			art_alternatives[key] = list( filter( lambda str: str != u'' , art_alternatives[key] ) )
			art_alternatives[key] = ' '.join(art_alternatives[key])

		art_alternatives = list( filter( lambda str: str != u'' , art_alternatives.values() ) )	

		article=' '.join(art_alternatives)
		# print article
		(day,month,year) = response.css('time.left::text').extract()[0].split('|')[1].split('.')
		time = year+"-"+month+"-"+day.strip()

		yield {
			'url': url,
			'title': title,
			'text': article,
			'date': time

		}	