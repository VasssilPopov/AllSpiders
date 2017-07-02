# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
# cd _AllSpiders
# Python RunBlitzSpider.py

'Get the yesterday date'
# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%Y.%m.%d").lower()

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

# input date
# '22. Юни 2017' --> 2017.06.22
def convertDate(aDate):
    aDate=aDate.replace(',','')
    dateParts=aDate.split()
    dateParts[1]=str(bgMonthstoNumber(dateParts[1]))
    aDate='%s.%s.%s'%(dateParts[2],dateParts[1],dateParts[0])
    return aDate


class BlitzSpider(scrapy.Spider):
	name = "Blitz"
	allowed_domains = ['www.blitz.bg','blitz.bg']
	start_urls = [
		"https://www.blitz.bg/svyat",
		"http://www.blitz.bg/politika",
		"https://www.blitz.bg/obshtestvo",
		"https://www.blitz.bg/ikonomika",
		"https://www.blitz.bg/kriminalni",
		"https://www.blitz.bg/intsidenti",
		"https://www.blitz.bg/zdrave",
		"https://www.blitz.bg/lyubopitno",
		"https://www.blitz.bg/layfstayl"
		
	]
	custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8'
	}
	
	def __init__(self):
		self.json_datafile = 'Blitz/Reports/Blitz-'+Today+'.json'
		self.links_seen = read_ids(self.json_datafile)
		'take only the end of the Mediapool url. The number after the news string:'
		self.links_seen = map(lambda url: url.split('news')[1] , self.links_seen)
		print '-'*10,'Blitz v(1.0)','-'*10

	def parse(self, response):

		urls=response.xpath('//article[@class="simple-post simple-big clearfix"]/a/@href | //header[@class="news-details"]/h3[@class="news-title"]/a/@href').extract()
		print "url: %s selected: %d" %(response.url, len(urls))
		for url in urls:
			if url.split('news')[1] not in self.links_seen:
				url = response.urljoin(url)
				yield scrapy.Request(url=url, callback=self.parse_details)

		# follow pagination link
		next_page_url=response.xpath('//div[@class="row pagination"]/div[2]/a[@class="btn next pull-right"]/@href').extract_first()
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
		pubDate = convertDate(pubDate)
		# print '>>', pubDate, strToday
		# articleDate=translateDateBG_EN(pubDate.split(',')[0])
		# print 'artDate: %s url= %s ' %(articleDate, url)
		# Filter on todays date
		print pubDate, strToday,(pubDate == strToday)
		if (pubDate == strToday):
			print 'saved :%s'% (url)
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': pubDate

			}
		else:
			raise CloseSpider('Index date changed')

