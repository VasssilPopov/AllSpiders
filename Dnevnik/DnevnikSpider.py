# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import date, timedelta
import os.path


yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
translateMonth={u'януари':'january',u'февруари':'february',u'март':'march',u'април':'april',u'май':'may',u'юни':'june',u'юли':'july',u'август':'august',u'септември':'september',u'октомври':'october',u'ноември':'november',u'декември':'december'}
def bgMonthstoNumber(monthName):
    monthName=monthName.lower()
    months= {u'януари':'01',u'февруари':'02', u'март':'03',
             u'април':'04',u'май':'05', u'юни':'06',
             u'юли':'07',u'август':'08', u'септември':'09',
             u'октомври':'10',u'ноември':'11', u'декември':'12'}

    if (monthName in months):
        return months[monthName]
    else:
        return'??'
	
class DnevnikSpider(scrapy.Spider):
    name = "Dnevnik"
    # start_urls = ["http://m.dnevnik.bg/allnews/"+yesterday.strftime("%Y/%m/%d")]
    start_urls = ["http://dnevnik.bg/allnews/yesterday/"]
    count = 0
    custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8',
		'DOWNLOAD_DELAY':'2',
		'COOKIES_ENABLED':'False',
		'CONCURRENT_REQUESTS_PER_DOMAIN':'1',
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

		title = response.xpath('//div[@class="content"]/h1/text() | //aside/div[@class="module"]/div[@class="site-block"]/div[@class="the-picture-summary article"]/h2/text()').extract_first()
		
		article=u' '.join(response.xpath('//div[@class="article-content"]/p/text()| //div[@class="article-content"]/h2/text() | //div[@class="article-content"]/p/a/text()| //div[@class="article-content"]/div[@class="story"]/p/text() | //div[@class="article-content"]/div[@class="story"]/text()').extract())
		# 'extract and prepare Article date'
		pubDate = response.xpath('//div[@class="article-tools"]/time/text()').extract_first()
		dateParts=pubDate.split()
		#tDate=translateMonth[dateParts[2]]
		#articleDate = ('%s-%s-%s' %(dateParts[1],tDate,'20'+dateParts[3])).lower()
		articleDate='%s.%s.%s'%('20'+dateParts[3],bgMonthstoNumber(dateParts[2]),dateParts[1])	
		yesterdaysDate=yesterday.strftime("%Y.%m.%d")
		self.count = self.count + 1
		# Filter on todays date
		if ((articleDate == yesterdaysDate) and ( len(article)) > 0):
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': articleDate
			}	
		else:
			pass