# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
import sys

# scrapy runspider 24chasaSpider.py -o Reports/24chasa-2017-05-17.json -t jsonlines
# RunIt 2017-05-17

'Get the yesterday date'
# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%Y.%m.%d")

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

def translateDateBG_EN(strDate):

    monthsBG_EN={u'януари':u'january',u'февруари':u'february',u'март':u'march',u'април':u'april',u'май':u'may',u'юни':u'june',u'юли':u'july',u'август':u'august',u'септември':u'september',u'октомври':u'october',u'ноември':u'november',u'декември':u'december'}

    dateParts=strDate.split()
    v=dateParts[1].lower()
    dateParts[1] = monthsBG_EN[v]
    result = ' '.join(dateParts[:3])
    return result

	
class Chasa24Spider(scrapy.Spider):
	name = "24chasa"
	# allowed_domains = ['https://www.24chasa.bg']
	allowed_domains = ['24chasa.bg']
	start_urls = [
		"https://www.24chasa.bg/novini/",
		# "https://www.24chasa.bg/sport/",
		# "https://www.24chasa.bg/region/",
		# "https://www.24chasa.bg/zdrave/",
		# "https://www.24chasa.bg/mnenia/",
		# "https://www.24chasa.bg/ojivlenie/",
	]
	custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8',
		'CONCURRENT_REQUESTS_PER_DOMAIN':'1',
		'DOWNLOAD_DELAY':'2',
		'COOKIES_ENABLED':'False',
		'DEPTH_LIMIT':'4'
	}
	
	def __init__(self):
		print '__init__'
		self.json_datafile = '24chasa/Reports/24chasa-'+Today+'.json'
		self.links_seen = read_ids(self.json_datafile)
		'take only the end of the Mediapool url. The number after the news string:'
		self.links_seen = set(map(lambda url: url.split('article/')[1] , self.links_seen))
		print '-'*10,'24 chasa v(1.0)','-'*10
		print 'seen: %d'% (len(self.links_seen))
		
		
	def parse(self, response):
		print 'parse'
		urls = response.xpath('//div[@class="entry-short"]/a/@href | //div[@class="entry-short last-item"]/a/@href').extract()

		print "depth: %d, url: %s selected: %d" %((response.meta['depth'] + 1), response.url, len(urls))
		# print "url: %s selected: %d" %( response.url, len(urls))
		for url in urls:
			code=url.split('article/')[1]
			
			if code not in self.links_seen:
				self.links_seen.add(code)
			url = response.urljoin(url)

			print '>>>', response.meta['depth'] ,url

			yield scrapy.Request(url=url, callback=self.parse_details)

		# follow pagination link
		next_page_url=response.xpath('//div[@id="page-left-content"]/div[@class="widget-left widget-entries "]/div[@class="widget-content"]/div[@class="pagination"]/a[last()]/@href').extract_first()
		if next_page_url:
			if (response.meta['depth'] == '4'):
				raise CloseSpider('Depth reached 4')

			next_page_url = response.urljoin(next_page_url)
			yield scrapy.Request(url=next_page_url, callback=self.parse)

	def parse_details(self, response):

		print 'parse_details'

	
		url     = response.url
		title   = response.xpath('//div[@id="page-left-content"]/div[@class="article"]/div[@class="head"]/h1/text()').extract_first().strip()

		article = u' '.join(response.xpath('//div[@id="text"]/span/p/text()').extract())
		
		pubDate=response.xpath('//div[@id="page-left-content"]/div[@class="article"]/div[@class="head"]/span[@class="article-date"]/span/text()').extract_first()
		# 21.06.2017 10:59
		(day, month, year)=pubDate.split(' ')[0].split('.')
		articleDate='%s.%s.%s'%(year, month, day)

		# articleDate=pubDate.split()[0]
		# print 'artDate: %s url= %s ' %(articleDate, url)
		# Filter on todays date
		print '>>>>', articleDate, strToday, (articleDate == strToday), url
		if (articleDate == strToday):
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': articleDate
			}
		else:
			pass
