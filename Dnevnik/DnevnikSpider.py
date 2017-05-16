# -*- coding: utf-8 -*-
import scrapy
import logging
import json
import sys
from sys import exit, path
import platform

if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\Spiders\Library')
else: 
	print 'Unknown platform' 
	exit() 

from ScrapingHelpers import *
from datetime import date, timedelta
import os
'$ scrapy crawl Dnevnik -o Dnevnik.json -t jsonlines'
'scrapy runspider DNSpider.py -o Dnevnik-28-Apr-2017.json -t json'
'scrapy runspider DNSpider3.py -o Dnevnik-28-Apr-2017.json -t json'

'Get the yesterday date'
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
translateMonth={u'януари':'january',u'февруари':'february',u'март':'march',u'април':'april',u'май':'may',u'юни':'june',u'юли':'july',u'август':'august',u'септември':'september',u'октомври':'october',u'ноември':'november',u'декември':'december'}


cwd = os.getcwd()
print cwd

class DnevnikSpider(scrapy.Spider):
	name = 'Dnevnik'
	allowed_domains = ['dnevnik.bg']
	custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
	
	def __init__(self):

		self.urls = ["http://m.dnevnik.bg/allnews/yesterday"]

		# Their date format is: http://www.dnevnik.bg/allnews/2017/03/19/
		# 'http://www.dnevnik.bg/rss/'

		self.json_datafile = 'Reports/Dnevnik-'+Yesterday+'.json'
		self.links_seen = self.get_ids(self.json_datafile)
		
		# Prepare links_seen data structure
		#self.links_seen=read_ids(self.json_datafile)

		print 'links_seen : %d' %(len(self.links_seen))
		
		
	def get_ids(self, json_datafile):
		ids = []
		
		try:
			ids = read_ids(json_datafile)
		except (IOError,ValueError):
			return set(ids)

		return set(ids)

	def start_requests(self):

		for url in self.urls:
			yield scrapy.Request(url=url, callback=self.parse)    

	def parse(self, response):
		'We need the titles, links and times to index and follow'

		# If we start from the rss
		# titles = response.xpath('//item/title/text()').extract()
		# links  = response.xpath('//item/link/text()' ).extract()
		# 
		links = response.css('div.text h2 a::attr(href)').extract()
		links = list (map( lambda str: 'http://www.dnevnik.bg'+str, links))		
		
		for link in links:
			if link not in self.links_seen:
				yield scrapy.Request(url=link, callback=self.parse_page)

	def parse_page(self, response):
		url   = response.url
		try:
			title = response.css('div.content>h1::text').extract()[0].strip()
		except:
			title = ""
		# art_alternatives = {}
		# art_alternatives[0] = response.css('div.article::text').extract()
		# art_alternatives[1] = response.css('div.article span::text').extract()
		# art_alternatives[2] = response.css('div.article div.story::text').extract()
		# art_alternatives[3] = response.css('div.gallery p::text').extract()

		# for key in art_alternatives:
		# 	art_alternatives[key] = list( map   ( lambda str: str.strip(), art_alternatives[key] ) )
		# 	art_alternatives[key] = list( filter( lambda str: str != u'' , art_alternatives[key] ) )
		# 	art_alternatives[key] = ' '.join(art_alternatives[key])

		# art_alternatives = list( filter( lambda str: str != u'' , art_alternatives.values() ) )	

		# # assert len(art_alternatives) == 1, 'Issue with %s'%url		
		
		article = ''.join(response.css('div.article-content>p::text').extract()).strip()

		#pubDate=response.xpath('//div[@class="info wbig"]/text()').extract_first()
		pubDate=response.xpath('//div[@class="article-tools"]/time/text()').extract_first()
		
		#extract and prepare Article date
		dateParts=pubDate.split()
		pubDate= ('%s-%s-%s' %(dateParts[1],dateParts[2],'20'+dateParts[3])).lower()
		articleDate=pubDate.replace(dateParts[2],translateMonth[dateParts[2]])
		todaysDate=yesterday.strftime("%d-%b-%Y").lower()
		
		# Filter on todays date
		if (articleDate == todaysDate):
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': pubDate

			}	
