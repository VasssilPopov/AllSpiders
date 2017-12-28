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
	
class StandartNewsSpider(scrapy.Spider):
	name = "StandartNews"
	allowed_domains = ['StandartNews.com']
	start_urls = [
		"http://standartnews.com/balgariya.html"
	]
	custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8'
	}
	pubDate = ''
	def __init__(self):
		self.json_datafile = 'StandartNews/Reports/StandartNews-'+Today+'.json'
		self.links_seen = read_ids(self.json_datafile)
		'take only the end of the StandartNews url. The number after the news string:'
		# self.links_seen = map(lambda url: url.split('news')[1] , self.links_seen)
		print '-'*10,'StandartNews v(1.0)','-'*10

	def parse(self, response):
	
		links=response.xpath('//div[@class="single_news_list_small"]/div[@class="news_content_list"]')

		print "url: %s selected: %d" %(response.url, len(links))
		for link in links:
		
			url=link.xpath('h2/a[@class="title_news_list"]/@href').extract_first()
			
			pubDate=link.xpath('comment()').extract_first()
			#date extraction and format 
			(day, month, year)=pubDate.split('|')[1].strip().split('.')
			pubDate='%s.%s.%s' % (year, month, day)
			
			print pubDate, strToday,pubDate == strToday
			if (pubDate == strToday):
				url = response.urljoin(url)
				print '>1>',url
				# logger.info('URL: %s', url)
				if url not in self.links_seen:
					# url = response.urljoin(url)
					print '>2>',url

					yield scrapy.Request(url=url, callback=self.parse_details)

		# follow pagination link
		next_page_url=response.xpath('//tr/td/a[@rel="next"]/@href').extract_first()
		print 'next_page_url: %s' % (next_page_url)
		if next_page_url:
			next_page_url = response.urljoin(next_page_url)
			print 'next_page_url: %s' % (next_page_url)
			yield scrapy.Request(url=next_page_url, callback=self.parse)

	def parse_details(self, response):

		print 'Mark-1'
		url     = response.url
		
		pageTitle=response.xpath('//div[@id="articleContentHolder"]/div/h2/text()').extract_first().strip()

		texts=response.xpath('//div[@id="articleContentHolder"]/div/div/div["articlBodyHolder"]/p/text()').extract()
		pageText=u' '.join(texts)
		
		
		pageDate=pubDate
		
		# print 'pageDate: %s url= %s ' %(pageDate, url)
		# Filter on todays date
		print pageDate, strToday,(pageDate == strToday), url
		if (pageDate == strToday):
			yield {
				'url': url,
				'title': pageTitle,
				'text': pageText,
				'date': pageDate
			}
		else:
			raise CloseSpider('Index date changed')

