# -*- coding: utf-8 -*-
import scrapy
import logging
from datetime import date, timedelta
import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
# cd _AllSpiders
# Python RunClubZSpider.py

'Get the yesterday date'
# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%Y.%m.%d").lower()
logger = logging.getLogger('myLogger')

def read_ids(file):

    'Read latest 11 chars from urls of the already processed publications '
    ids=set()

    try:
        with open(file, 'rb') as f:
            for item in json_lines.reader(f):
                ids.add(item["url"])
    except IOError:
        ids = set()
	# print 'error'

    return ids
	
class ClubZSpider(scrapy.Spider):
	name = "clubz"
	allowed_domains = ['clubz.bg']
	start_urls = [
		"http://clubz.bg/news"
	]
	custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8',
        'DEPTH_LIMIT':'2'
	}
	
	def __init__(self):
		self.json_datafile = 'ClubZ/Reports/ClubZ-'+Today+'.json'
		self.links_seen = read_ids(self.json_datafile)
		'take only the end of the ClubZ url. The number after the news string:'
		# self.links_seen = map(lambda url: url.split('news')[1] , self.links_seen)
		print '-'*10,'ClubZ v(1.0)','-'*10

	def parse(self, response):

		urls=response.xpath('//div[@class="views-field views-field-title"]/span[@class="field-content"]/a/@href').extract()
		print "url: %s selected: %d" %(response.url, len(urls))
		for url in urls:
			url = response.urljoin(url)
			# print '>1>',url
			# logger.info('URL: %s', url)
			if url not in self.links_seen:
				# url = response.urljoin(url)
				yield scrapy.Request(url=url, callback=self.parse_details)

		# follow pagination link
		# next_page_url=response.xpath('//div[@class="row pagination"]/div[2]/a[@class="btn next pull-right"]/@href').extract_first()
        next_page_url = response.xpath('//ul[@class="pagination"]/li[@class="next"]/a/@href').extract()
        
        if next_page_url:
			next_page_url = response.urljoin(next_page_url)
            # yield scrapy.Request(url=next_page_url, callback=self.parse)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
            

	def parse_details(self, response):

		url     = response.url
		
		pageTitle=response.xpath('//div[@class="views-field views-field-title"]/span[@class="field-content"]/a/text()').extract_first()

		# pageText=response.xpath('//div[@class="views-field views-field-body"]/div[@class="field-content"]/p/text()').extract()
		pageText=response.xpath('//div[@class="views-field views-field-body"]/div[@class="field-content"]/p/text() | //div[@id="not-first"]/div/a/text()').extract()
		pageText=u' '.join(pageText)

		pageDate=response.xpath('//div[@class="views-field views-field-published-at"]/span[@class="field-content"]/text()').extract_first()
		# pageDate = pageDate.split(',')[0]
		(day,month,year)=pageDate.split(',')[0].split('.')
		pageDate='%s.%s.%s'%(year,month,day)
		
		# print 'pageDate: %s url= %s ' %(pageDate, url)
		# Filter on todays date
		print pageDate, strToday,(pageDate == strToday), url
		# print 'Mark-1'
		if (pageDate == strToday):
			yield {
				'url': url,
				'title': pageTitle,
				'text': pageText,
				'date': pageDate
			}
		# else:
			# raise CloseSpider('Index date changed')

