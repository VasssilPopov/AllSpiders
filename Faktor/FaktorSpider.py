# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
import sys

# scrapy runspider FaktorSpider.py -o Reports/Faktor-2017-05-17.json -t jsonlines

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

    return ids
def getDate( response ):
        pubDate=u''.join(response.xpath('//article[@class="entry single"]/span[@class="entry-date"]/text()').extract()).strip()

        pubDate2 =  response.xpath('//article[@class="entry single"]/span[@class="entry-date"]/span/text()').extract()
        monthName=pubDate2[0][0:3].lower()

        months= {'jan':'01', 'feb':'02', 'mar':'03', 'apr':'04', 'may':'05', 'jun':'06', 'jul':'07', 'aug':'08', 'sep':'09', 'oct':'10', 'nov':'11', 'dec':'12'}
        dateExpr = '????.??.??'
        if (monthName in months):
                montNumber = months[monthName]
                dateExpr =  '%s.%s.%s' % (pubDate2[1],montNumber, pubDate)

        return dateExpr
class FaktorSpider(scrapy.Spider):
	name = "faktor.bg"
	allowed_domains = ['faktor.bg']
	start_urls = [
		"https://www.faktor.bg/bg/articles/novini/",
		# "http://www.faktor.bg/bg/articles/novini/",
		# "https://www.24chasa.bg/sport/",
		# "https://www.24chasa.bg/region/",
		# "https://www.24chasa.bg/zdrave/",
		# "https://www.24chasa.bg/mnenia/",
		# "https://www.24chasa.bg/ojivlenie/",
	]
	custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8',
		'CONCURRENT_REQUESTS_PER_DOMAIN':'1',
		'DOWNLOAD_DELAY':'5',
		'COOKIES_ENABLED':'False',
		'DEPTH_LIMIT':'4'
	}
	

	# def __init__(self):
		# print '__init__'
		# self.json_datafile = 'Faktor/Reports/Faktor-'+Today+'.json'
		# self.links_seen = read_ids(self.json_datafile)
		# 'take only the end of the Mediapool url. The number after the news string:'
		# #self.links_seen = set(map(lambda url: url.split('article/')[1] , self.links_seen))
		# print '-'*10,'24 chasa v(1.0)','-'*10
		# print 'seen: %d'% (len(self.links_seen))
		
		
	def parse(self, response):
        
		print 'parse'
		urls = response.xpath('//article[@class="entry"]/div[@class="row"]/div/h2[@class="entry-title"]/a/@href').extract()

		print "depth: %d, url: %s selected: %d" %((response.meta['depth'] + 1), response.url, len(urls))
		# print "url: %s selected: %d" %( response.url, len(urls))

		for url in urls:
		
			# if url not in self.links_seen:
				# self.links_seen.add(url)
                
			url = response.urljoin(url)

			yield scrapy.Request(url=url, callback=self.parse_details)

		## follow pagination link
        
		# next_page_url=response.xpath('//div[@id="page-left-content"]/div[@class="widget-left widget-entries "]/div[@class="widget-content"]/div[@class="pagination"]/a[last()]/@href').extract_first()
		# if next_page_url:
			# if (response.meta['depth'] == '4'):
				# raise CloseSpider('Depth reached 4')

			# next_page_url = response.urljoin(next_page_url)
			# yield scrapy.Request(url=next_page_url, callback=self.parse)

	def parse_details(self, response):

		print 'parse_details'

	
		url     = response.url
        
		title = response.xpath('//div[@class="entry-media"]/h1/text()').extract_first()
        
		texts=response.xpath('//article[@class="entry single"]/div[@class="entry-content"]/p/text()').extract()
		article = u' '.join(texts)
		
		pubDate = getDate(response)
		# pubDate=response.xpath('//div[@id="page-left-content"]/div[@class="article"]/div[@class="head"]/span[@class="article-date"]/span/text()').extract_first()
		# # 21.06.2017 10:59
		(year, month, day)=pubDate.split('.')
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
