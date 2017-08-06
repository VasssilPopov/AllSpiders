# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import date, timedelta
import os.path
from scrapy.exceptions import CloseSpider


yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y.%m.%d")
today=date.today()
Today=today.strftime("%Y-%m-%d")

class SegaBGSpider(scrapy.Spider):
    name = "SegaBG"
    start_urls = ["http://www.segabg.com/index.php?iid=12527&sid=2",
				"http://www.segabg.com/index.php?iid=12527&sid=3",
				"http://www.segabg.com/index.php?iid=12527&sid=4",
				"http://www.segabg.com/index.php?iid=12527&sid=5", 
				"http://www.segabg.com/index.php?iid=12527&sid=6",
				"http://www.segabg.com/index.php?iid=12527&sid=12",
	]
    count = 0
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
		'CONCURRENT_REQUESTS_PER_DOMAIN':'1',
		'DOWNLOAD_DELAY':'5',
		'COOKIES_ENABLED':'False',
		# 'DEPTH_LIMIT':'3'
	}

	
    def __init__(self):
		# "Empty output file"
		fileName="SegaBG/Reports/SegaBG-%s.json"%(Today)
		f = open(fileName, 'w').close()
		print '-'*10,'SegaBG v(2.0)','-'*10
    def parse(self, response):

 		urls=response.xpath('//tr/td/div[@class="article"]/div[@class="a_title"]/a/@href').extract()
		print "url: %s selected: %d" %(response.url, len(urls))

		for url in urls:
			url = response.urljoin(url)
			yield scrapy.Request(url=url, callback=self.parse_page)
		
    def parse_page(self, response):
		months= {u'януари':'01',u'февруари':'02', u'март':'03',
		 u'април':'04',u'май':'05', u'юни':'06',
		 u'юли':'07',u'август':'08', u'септември':'09',
		 u'октомври':'10',u'ноември':'11', u'декември':'12'}

		url = response.url
		title=response.xpath('//div[@class="article"]/div[@class="a_title"]/h3[@class="a_title"]/text()').extract_first()

		text = response.xpath('//div[@class="article"]/div[@class="a_content"]/text()').extract()
		article = u' '.join(text)
		
		
		# 'extract and prepare Article date'
		date=response.xpath('//div[@id="issue_number"]/text()').extract()
		pubDate=u' '.join(date)
		parts= pubDate.split()
		(day, month, year)=parts[-3:]
		month=months[month.lower()]
		articleDate = '%s.%s.%s'%(year,month,day)
		if articleDate == Yesterday:
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': articleDate
			}	
