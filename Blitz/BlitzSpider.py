# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
# scrapy runspider BlitzSpider.py -o Reports/PIK-2017-05-17.json -t jsonlines
# RunIt 2017-05-17

'Get the yesterday date'
# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%d %B %Y").lower()
#----------------------------------------------------
print 'Version: ',0.2
#----------------------------------------------------

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

	
class BlitzSpider(scrapy.Spider):
	name = "Blitz"
	allowed_domains = ['www.blitz.bg']
	start_urls = [
		"http://www.blitz.bg/politika"
	]
	custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8'
	}
	
	def __init__(self):
		print os.getcwd()
		self.json_datafile = 'Blitz/Reports/Blitz-'+Today+'.json'
		self.links_seen = read_ids(self.json_datafile)
		'take only the end of the Mediapool url. The number after the news string:'
		self.links_seen = map(lambda url: url.split('news')[1] , self.links_seen)
		print 'links_seen:', len(self.links_seen)

	def parse(self, response):

		urls=response.xpath('//article[@class="simple-post simple-big clearfix"]/a/@href | //header[@class="news-details"]/h3[@class="news-title"]/a/@href').extract()
		for url in urls:
			if url.split('news')[1] not in self.links_seen:
				url = response.urljoin(url)
				yield scrapy.Request(url=url, callback=self.parse_details)

		# follow pagination link
		next_page_url=response.xpath('//div[@class="row pagination"]/div[2]/a[@class="btn next pull-right"]/@href').extract_first()
		print 'next_page_url: ', next_page_url
		if next_page_url:
			next_page_url = response.urljoin(next_page_url)
			yield scrapy.Request(url=next_page_url, callback=self.parse)

	def parse_details(self, response):

		url     = response.url
		
		title   = response.xpath('//header/h1[@class="post-title"]/text()').extract()[0].strip()

		introStr = response.xpath('//div[@class="intro"]/text()').extract()[0].strip()
		texts= ' '.join(response.xpath('//div[@id="articleContent"]/strong/text() | //div[@id="articleContent"]/text()| //div[@id="articleContent"]/p/strong/text()| //div[@id="articleContent"]/p/text()').extract())
		article = introStr + texts

		pubDate=response.xpath('//*[@id="page-container"]/div[1]/div/div/article/header/div/ul/li[2]/text()').extract_first()
	
		articleDate=translateDateBG_EN(pubDate.split(',')[0])
		print 'articleDate: ', articleDate, 'strToday: ', strToday, (articleDate == strToday)
		# Filter on todays date
		if (articleDate == strToday):
			print 'save data'
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': pubDate

			}
		else:
			raise CloseSpider('Index date changed')
		print '--done--'

