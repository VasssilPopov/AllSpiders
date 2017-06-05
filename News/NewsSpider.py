# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
import os
import json
import json_lines
from scrapy.exceptions import CloseSpider
from scrapy.spiders import Rule
#from scrapy.linkextractors import Linkextractor

# scrapy runspider OffNewsSpider.py -o Reports/OffNews-2017-05-17.json -t jsonlines
# RunIt 2017-05-17

'Get the yesterday date'
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%d %b %Y").lower()



class NewsSpider(scrapy.Spider):
	


	name = "news"
	start_urls = ['https://news.bg/yesterday']

	
	def parse(self, response):


		# "Empty output file"
		fileName="Reports/News-%s.json"%(Yesterday)
		f = open(fileName, 'w').close()

		urls = response.xpath('//div[@id="content-main"]/div[@class="inner-page"]/div[@class="main-news"]/a[@class="main-thumb"]/@href | //div[@class="topic"]/div[@class="topic-information"]/h2/a[@class="title"]/@href').extract()
		for url in urls:
			url = response.urljoin(url)
			yield scrapy.Request(url=url, callback=self.parse_details)

		print '>> follow pagination link: '
		# follow pagination link
		#next_page_url=response.xpath('//ul[@class="pagination"]/li[@rel="next"]/a/@href')
		next_page_url=response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').extract_first()
		print next_page_url
		if next_page_url:
			next_page_url = response.urljoin(next_page_url)
			yield scrapy.Request(url=next_page_url, callback=self.parse)
			
	def parse_details(self, response):
		
		url = response.url
		pageTitle = response.xpath('//div[@id="content-main"]/article[@class="article-inner"]/header/h1/text()').extract_first()
		pageTexts = response.xpath('//div[@id="content-main"]/article[@class="article-inner"]/div[@class="article-text"]')
		pageText = pageTexts.xpath('p/text() | p/strong/text()').extract()
		pageText=''.join(pageText)
		yield {
			'url': url,
			'title': pageTitle,
			'text': pageText,
			'date': Yesterday
        }