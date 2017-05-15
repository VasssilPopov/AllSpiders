# -*- coding: utf-8 -*-
import scrapy
import logging
import json
from sys import exit, path
from datetime import date, timedelta
import urllib
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

# scrapy runspider PIKSpider.py -o PIK-2017-05-17.json -t jsonlines
# RunIt 2017-05-17

'Get the yesterday date'
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")

class PIKSpider(scrapy.Spider):
	name = 'PIK'
	allowed_domains = ['pik.bg']


	custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

	def __init__(self):
		self.urls = ["http://pik.bg/политика-cat6.html"]
		self.json_datafile = 'Reports/PIK-'+Today+'.json'
		self.links_seen = read_ids(self.json_datafile)

	def start_requests(self):

		for url in self.urls:
			yield scrapy.Request(url=url, callback=self.parse)    

	def parse(self, response):
	
		# 'We need the titles, links and times to index and follow'
		links=response.xpath('//div[@class="right_part"]/a/@href').extract()

		for link in links:
			if quote( link.encode('utf-8') ).replace("%3A", ':').replace("%26quot",'') not in self.links_seen:
				# print link
				# print quote( link.encode('utf-8') ).replace("%3A", ':').replace("%26quot",'')
				yield scrapy.Request(url=link, callback=self.parse_page)

	def parse_page(self, response):

		url   = response.url
		title = response.xpath('//*[@id="hdscrolll"]/div/text()').extract_first()
		
		art_alternatives = {}
		art_alternatives[0] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/text()|//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/a/span/strong/text()').extract()
		art_alternatives[1] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/span/text()').extract()
		art_alternatives[2] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div[@class="lead"]/p/text()').extract()

		for key in art_alternatives:
			art_alternatives[key] = list( map   ( lambda str: str.strip(), art_alternatives[key] ) )
			art_alternatives[key] = list( filter( lambda str: str != u'' , art_alternatives[key] ) )
			art_alternatives[key] = ' '.join(art_alternatives[key])

		art_alternatives = list( filter( lambda str: str != u'' , art_alternatives.values() ) )	

		article=' '.join(art_alternatives)
		
		(day,month,year) = response.css('time.left::text').extract()[0].split('|')[1].split('.')
		time = year+"-"+month+"-"+day

		yield {
			'url': url,
			'title': title,
			'text': article,
			'time': time

		}	
