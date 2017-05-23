# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import date, timedelta
from sys import exit, path
from datetime import date, timedelta
import platform

if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
translateMonth={u'януари':'january',u'февруари':'february',u'март':'march',u'април':'april',u'май':'may',u'юни':'june',u'юли':'july',u'август':'august',u'септември':'september',u'октомври':'october',u'ноември':'november',u'декември':'december'}

class DnevnikSpider(scrapy.Spider):
    name = "Dnevnik"
    start_urls = ["http://m.dnevnik.bg/allnews/"+yesterday.strftime("%Y/%m/%d")]

    def parse(self, response):
		# 'Remove report file if it exists'
		fileName="Reports/Dnevnik-%s.json"%(Yesterday)
		try:
			os.remove(fileName)
		except OSError:
			pass
		
 		# urls = response.xpath('//div[@class="quote"]/span/a/@href').extract()
		urls=response.xpath('//article[@class="secondary-article-v2 border-top list-item"]/div[@class="text"]/h2/a/@href').extract()
		
		for url in urls:
			url = response.urljoin(url)
			yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
		url = response.url
		# title = response.css('div.content>h1::text').extract()[0].strip()
		title = response.xpath('//div[@class="content"]/h1/text()').extract_first()
		# title = unicode(title,"unicode-escape")
		# article = ''.join(response.css('div.article-content>p::text').extract()).strip()

		article = ''.join(response.xpath('//div[@class="article-content"]/p/text()').extract()).strip()
		
		# article = unicode(article,"unicode-escape")
		pubDate=response.xpath('//div[@class="article-tools"]/time/text()').extract_first()
		
		#extract and prepare Article date
		dateParts=pubDate.split()
		pubDate= ('%s-%s-%s' %(dateParts[1],dateParts[2],'20'+dateParts[3])).lower()
		articleDate=pubDate.replace(dateParts[2],translateMonth[dateParts[2]])
		todaysDate=yesterday.strftime("%d-%b-%Y").lower()
		
		# Filter on todays date
		if (articleDate == todaysDate):
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': pubDate

			}	
		
