# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
# scrapy runspider 24chasaSpider.py -o Reports/24chasa-2017-05-17.json -t jsonlines
# RunIt 2017-05-17

'Get the yesterday date'
# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
# strToday = today.strftime("%d.%m.%Y")
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

# def translateDateBG_EN(strDate):

    # monthsBG_EN={u'януари':u'january',u'февруари':u'february',u'март':u'march',u'април':u'april',u'май':u'may',u'юни':u'june',u'юли':u'july',u'август':u'august',u'септември':u'september',u'октомври':u'october',u'ноември':u'november',u'декември':u'december'}

    # dateParts=strDate.split()
    # v=dateParts[1].lower()
    # dateParts[1] = monthsBG_EN[v]
    # result = ' '.join(dateParts[:3])
    # return result

	
class TrudSpider(scrapy.Spider):
	name = "trud"
	allowed_domains = ['trud.bg']
	start_urls = [
		"https://trud.bg/news/"
	]
	custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8'
	}
	
	def __init__(self):
		self.json_datafile = 'Trud/Reports/Trud-'+Today+'.json'
		
		print '-'*10,'Trud v(1.0)','-'*10
		self.links_seen = read_ids(self.json_datafile)
		print 'seen: %d'% (len(self.links_seen))
		'take only the end of the url. The number after the news string:'
		# self.links_seen = map(lambda url: url.split('article/')[1] , self.links_seen)
		
		
	def parse(self, response):

		urls = response.xpath('//ol[@class="list-of-entities clearfix"]/li/div[@class="story-item-link"]/div[@class="story-item-body"]/h3[@class="story-item-body-headline"]/a/@href').extract()
		
		for url in urls:
			# code=url.split('article/')[1]
			if url not in self.links_seen:
				url = response.urljoin(url)
				self.links_seen.add(url)
				yield scrapy.Request(url=url, callback=self.parse_details)
		# NO pagination
		# # follow pagination link
		# next_page_url=response.xpath('//div[@id="page-left-content"]/div[@class="widget-left widget-entries "]/div[@class="widget-content"]/div[@class="pagination"]/a[last()]/@href').extract_first()
		# if next_page_url:
			# next_page_url = response.urljoin(next_page_url)
			# yield scrapy.Request(url=next_page_url, callback=self.parse)

	def parse_details(self, response):
	
		url     = response.url
		
		title   = response.xpath('//header[@class="article-header"]/h1[@class="headline-heading"]/text()').extract_first()
        texts=response.xpath('//div[@class="article-content"]/p/text()').extract()
		article = u' '.join(texts)
		pubDate=response.xpath('//time[@class="entry-time meta-property--date"]/span[@class="meta-property--date-date"]/text()').extract_first()
		# 23.06.2017

		(day, month, year) = pubDate.split('.')
		articleDate = '%s.%s.%s'%(year, month, day)
		
		# dateParts=pubDate.split('.')
		# tmp=dateParts[0]
		# dateParts[0]=dateParts[2]
		# dateParts[2]=tmp
		# articleDate='.'.join(dateParts)
		# Filter on todays date
		print articleDate,strToday,(articleDate == strToday)
		if (articleDate == strToday):

			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': articleDate
			}
		else:
			raise CloseSpider('Index date changed')

