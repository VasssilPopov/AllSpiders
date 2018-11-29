# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
# scrapy runspider 24chasaSpider.py -o Reports/24chasa-2017-05-17.json -t jsonlines
# RunIt 2017-05-17

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
                ids.add(item["url"].split('node/')[1])
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
    aDate=aDate.replace('.','')
    dateParts=aDate.split()
    dateParts[1]=str(bgMonthstoNumber(dateParts[1]))
    aDate='%s.%s.%s'%(dateParts[2],dateParts[1],(u'00'+dateParts[0])[-2:])
    return aDate
    
	
class DumaSpider(scrapy.Spider):
	name = "Duma"
	# allowed_domains = ['http://Duma.bg']
	start_urls = [
		"http://duma.bg/taxonomy/term/1",
		"http://duma.bg/taxonomy/term/2",
		"http://duma.bg/taxonomy/term/3/1",
		"http://duma.bg/taxonomy/term/4/1",
		"http://duma.bg/taxonomy/term/5/1",
		"http://duma.bg/taxonomy/term/6/1",
	]
	custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8',
		'CONCURRENT_REQUESTS_PER_DOMAIN':'1',
#		'DOWNLOAD_DELAY':'3',
		'COOKIES_ENABLED':'False',
#        'DEPTH_LIMIT':'2'
	}
	
	def __init__(self):
		self.json_datafile = 'Duma/Reports/Duma-'+Today+'.json'
		self.links_seen = read_ids(self.json_datafile)
		'take only the end of the Mediapool url. The number after the news string:'
		# self.links_seen = map(lambda url: url.split('node/')[1] , self.links_seen)
		# print 'point 2: ',type(self.links_seen)
		print '-'*10,'Duma v(1.0)','-'*10
		print 'seen: %d'% (len(self.links_seen))
		
	def parse(self, response):
		urls=response.xpath('//div[@class="views-field-title"]/span[@class="field-content"]/a/@href').extract()
		print "url: %s selected: %d" %(response.url, len(urls))
		for url in urls:
			code=url.split('node/')[1]
			if code not in self.links_seen:
				# print url
				self.links_seen.add(code)
				urlTemp = response.urljoin(url)
				yield scrapy.Request(url=urlTemp, callback=self.parse_details)

		# follow pagination link
		next_page_url= response.xpath('//div[@class="item-list"]/ul[@class="pager"]/li[@class="pager-next"]/a[@class="active"]/@href').extract_first()
        
		if next_page_url:
			next_page_url = response.urljoin(next_page_url)
			print 'next page url: %s' % (next_page_url)
			yield scrapy.Request(url=next_page_url, callback=self.parse)

	def parse_details(self, response):
		url     = response.url
		title = response.xpath('//div[@class="container"]/p[@class="title"]/a/text()').extract_first()
		
		text = response.xpath('//div[@class="container"]/div[@class="meta"]/div[@class="content"]/p/text() | //div[@class="container"]/div[@class="meta"]/div[@class="content"]/p/strong/text()').extract()
		article = u' '.join(text)
		
		pubDate =response.xpath('//div[@class="container"]/div[@class="meta"]/span[@class="date-display-single"]/text()').extract_first()
		# 21.06.2017 10:59
		
		pubDate=convertDate(pubDate)
		# print 'artDate: %s url= %s ' %(articleDate, url)
		# Filter on todays date
		print pubDate, strToday, (pubDate == strToday), url
		if (pubDate == strToday):
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': pubDate

			}
		# else:
			# raise CloseSpider('Index date changed')

