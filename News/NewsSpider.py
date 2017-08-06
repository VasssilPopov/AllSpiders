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
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%d %b %Y").lower()

class NewsSpider(scrapy.Spider):

	name = "news"
	start_urls = ['https://news.bg/yesterday']
	custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8',
		'DOWNLOAD_DELAY':'5',
		'COOKIES_ENABLED':'False',
	}

	def __init__(self):
	
		# "Empty output report file."
		fileName="News/Reports/News-%s.json"%(yesterday.strftime("%Y-%m-%d"))
		f = open(fileName, 'w').close()
		
		print '-'*10,'News v(1.0)','-'*10
 
	def parse(self, response):

		urls = response.xpath('//div[@id="content-main"]/div[@class="inner-page"]/div[@class="main-news"]/a[@class="main-thumb"]/@href | //div[@class="topic"]/div[@class="topic-information"]/h2/a[@class="title"]/@href').extract()
		print "url: %s selected: %d" %(response.url, len(urls))
		for url in urls:
			url = response.urljoin(url)
			yield scrapy.Request(url=url, callback=self.parse_details)

		# follow pagination link
		next_page_url=response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').extract_first()
		if next_page_url:
			next_page_url = response.urljoin(next_page_url)
			yield scrapy.Request(url=next_page_url, callback=self.parse)
			
	def parse_details(self, response):
		
		url = response.url
		
		pageTitle = response.xpath('//div[@id="content-main"]/article[@class="article-inner"]/header/h1/text()').extract_first()
		
		pageText = response.xpath('//div[@id="content-main"]/article[@class="article-inner"]/div[@class="article-text"]/p/text() | //div[@id="content-main"]/article[@class="article-inner"]/div[@class="article-text"]/p/strong/text()').extract()
		
		pageText=u''.join(pageText)
		
		pageDate = response.xpath('//div[@id="content-main"]/article[@class="article-inner"]/header/div[@class="article-info"]/p[@class="time"]/@content').extract_first()
		pageDate=pageDate.split('T')
		pageDate=pageDate[0].replace('-','.')
		print pageDate,Yesterday, pageDate==Yesterday
		if (pageDate == Yesterday):
			# print 'saved'
			yield {
				'url': url,
				'title': pageTitle,
				'text': pageText,
				'date': pageDate
			}