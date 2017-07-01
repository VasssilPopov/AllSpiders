# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import date, timedelta
import os.path


yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
translateMonth={u'януари':'january',u'февруари':'february',u'март':'march',u'април':'april',u'май':'may',u'юни':'june',u'юли':'july',u'август':'august',u'септември':'september',u'октомври':'october',u'ноември':'november',u'декември':'december'}

	
class DnevnikSpider(scrapy.Spider):
    name = "Dnevnik"
    start_urls = ["http://m.dnevnik.bg/allnews/"+yesterday.strftime("%Y/%m/%d")]
    count = 0
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
	}
    def __init__(self):
		# "Empty output file"
		fileName="Dnevnik/Reports/Dnevnik-%s.json"%(Yesterday)
		f = open(fileName, 'w').close()
		print '-'*10,'Dnevnik v(1.0)','-'*10
    def parse(self, response):

 		urls=response.xpath('//article[@class="secondary-article-v2 border-top list-item"]/div[@class="text"]/h2/a/@href').extract()
		print "url: %s selected: %d" %(response.url, len(urls))

		for url in urls:
			url = response.urljoin(url)
			yield scrapy.Request(url=url, callback=self.parse_page)
		
    def parse_page(self, response):
		url = response.url
		title = response.xpath('//div[@class="content"]/h1/text()').extract_first()
		article=u''.join(response.xpath('//div[@class="article-content"]/p/text() | //div[@class="article-content"]/div[@class="story"]/p/text() | //div[@class="article-content"]/div[@class="story"]/text()').extract())

		# 'extract and prepare Article date'
		pubDate = response.xpath('//div[@class="article-tools"]/time/text()').extract_first()
		dateParts=pubDate.split()
		tDate=translateMonth[dateParts[2]]
		articleDate = ('%s-%s-%s' %(dateParts[1],tDate,'20'+dateParts[3])).lower()

		todaysDate=yesterday.strftime("%d-%B-%Y").lower()
		self.count = self.count + 1
		# Filter on todays date
		if ((articleDate == todaysDate) and ( len(article)) > 0):
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': articleDate

			}	
		else:
			pass