# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
import json
import json_lines
import os
from scrapy.exceptions import CloseSpider
from scrapy.spiders import Rule
# from scrapy.linkextractors import Linkextractor

# Python RunOffNewsSpider.py 

'Get the yesterday date'
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%d %b %Y").lower()


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

class OffNewsSpider(scrapy.Spider):
    name = "offnews"
    allowed_domains = ['m.offnews.bg']

	# https://m.offnews.bg/2017-06-28/
    start_urls = ['https://m.offnews.bg/'+Yesterday+'/']
    custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8'
	}
 
    def __init__(self):
		# "Empty output file"
		fileName="OffNews/Reports/OffNews-%s.json"%(Yesterday)
		f = open(fileName, 'w').close()
		print '-'*10,'OffNews v(1.0)','-'*10


    def parse(self, response):
		urls = response.xpath('//div[@class="content"]/div[@class="cat_list_s"]/div[@class="cat_list_s_int"]/div[@class="cat_list_s_title"]/a/@href').extract()
		print "url: %s selected: %d" %(response.url, len(urls))
		for url in urls:
			url = response.urljoin(url)
			yield scrapy.Request(url=url, callback=self.parse_details)

		# follow pagination link
		next_page_url = response.xpath('//div[@class="pageBox bb3y"]/a[@class="next"]/@href').extract_first()
		if next_page_url != '#':
			next_page_url = response.urljoin(next_page_url)
			yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):
        url=response.url
        if (url.startswith('http://mamaninja.bg/')):
		    return
        title = response.xpath('//div[@class="news_box"]/h1[@class="news_box_title"]/text()').extract_first()
        textStrong = response.xpath('//div[@class="newsdet"]/p/strong/text()').extract_first()
        texts = response.xpath('//div[@class="newsdet"]/p/strong/text() | //div[@class="newsdet"]/p/text()').extract()
        text = u''.join(texts)
        yield {
			'url': url,
			'title': title,
			'text': text,
			'date': Yesterday
		}
