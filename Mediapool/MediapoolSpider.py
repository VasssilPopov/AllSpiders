# -*- coding: utf-8 -*-
import scrapy
import logging
import json
from sys import exit, path
# path.append('/home/peio/dev/Scrapy')
path.append('C:\STUDY_PYTHON\Projects\LIBRARIES')
from ScrapingHelpers import *
from datetime import date, timedelta

# scrapy runspider MediapoolSpider.py -o Reports/Mediapool-30-Apr-2017.json -t json>Logs/output.txt
# runIt 2017-05-08

translateMonth={u'януари':'january',u'февруари':'february',u'март':'march',u'април':'april',u'май':'may',u'юни':'june',u'юли':'july',u'август':'august',u'септември':'september',u'октомври':'october',u'ноември':'november',u'декември':'december'}

'Get the today date'
today = date.today()
Today = today.strftime("%Y-%m-%d")

class MediapoolSpider(scrapy.Spider):
	name = 'Mediapool'
	allowed_domains = ['mediapool.bg', 'www.mediapool.bg']
	custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

	def __init__(self):

		self.urls = ["http://mediapool.bg/today.html"]
		self.json_datafile = 'Reports/Mediapool-'+Today+'.json'
		
		# Prepare links_seen data structure
		self.links_seen=[]
		

		try:
			# with open(self.json_datafile) as json_file:  
				# data = json.load(json_file)
			with open(self.json_datafile) as f:
				for line in f:
					json_data.append(json.loads(line))

			self.links_seen=[x['url'] for x in json_data]
		except:
			self.links_seen=[]
		
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

		# 'We need the titles, links and times to index and follow'
		links = response.xpath("//a[@class='news_in_a']/@href").extract()
	
		for link in links:
			if link not in self.links_seen:
				yield scrapy.Request(url=link, callback=self.parse_page)

				
	def parse_page(self, response):

		url     = response.url
		title   = response.xpath('//div[@class="main_left"]/h1/text()').extract()[0].strip()
 		article = ''.join(response.xpath('//div[@class="main_left"]/div/p/text()').extract()).strip()
		pubDate=response.xpath('//div[@class="info wbig"]/text()').extract_first()
		
		#extract and prepare Article date
		dateParts=pubDate.split()
		pubDate= ('%s-%s-%s' %(dateParts[2],dateParts[3],dateParts[4])).lower()
		articleDate=pubDate.replace(dateParts[3],translateMonth[dateParts[3]])
		todaysDate=date.today().strftime("%d-%b-%Y").lower()
		
		# Filter on todays date
		if (articleDate == todaysDate):
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': pubDate
			}	
