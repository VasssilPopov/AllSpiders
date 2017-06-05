# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
import json
import json_lines
import os
from scrapy.exceptions import CloseSpider
from scrapy.spiders import Rule
# from scrapy.linkextractors import Linkextractor

# scrapy runspider OffNewsSpider.py -o Reports/OffNews-2017-05-17.json -t jsonlines
# RunIt 2017-05-17

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

	# https://m.offnews.bg/2017-05-27/
    start_urls = ['https://m.offnews.bg/'+Yesterday+'/']
    custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8'
	}
    # rules = (
		# # Extract links matching 'category.php' (but not matching 'subsection.php')
		# # and follow links from them (since no callback means follow=True by default).
		# Rule(LinkExtractor(allow=('m.offnews.bg', ), deny=('mamaninja.bg', ))),
		# )

    def parse(self, response):
		# "Empty output file"
		fileName="Reports/OffNews-%s.json"%(Yesterday)
		f = open(fileName, 'w').close()

		urls = response.xpath('//div[@class="content"]/div[@class="cat_list_s"]/div[@class="cat_list_s_int"]/div[@class="cat_list_s_title"]/a/@href').extract()
		for url in urls:
			# if url[-11:] not in self.links_seen:
				# url = response.urljoin(url)
				# yield scrapy.Request(url=url, callback=self.parse_details)
			url = response.urljoin(url)
			yield scrapy.Request(url=url, callback=self.parse_details)

		# follow pagination link
		# next_page_url = response.css('li.next > a::attr(href)').extract_first()
		next_page_url = response.xpath('//div[@class="pageBox bb3y"]/a[@class="next"]/@href').extract_first()
		if next_page_url != '#':
			next_page_url = response.urljoin(next_page_url)
			yield scrapy.Request(url=next_page_url, callback=self.parse)
		print '-- DONE --'
    def parse_details(self, response):
		print '3.parse_details: '

		url=response.url
		
		title = response.xpath('//div[@class="news_box"]/h1[@class="news_box_title"]/text()').extract_first()
		textStrong = response.xpath('//div[@class="newsdet"]/p/strong/text()').extract_first()
			
		texts = response.xpath('//div[@class="newsdet"]/p/text()').extract()
		if textStrong:
			text = textStrong + u''.join(texts)
		else:
			text = u''.join(texts)
		yield {
				'url': url,
				'title': title,
				'text': text,
				'date': Yesterday
		}
