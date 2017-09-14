# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import date, timedelta
import platform
import sys
from sys import exit, path
from datetime import date, timedelta
if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 
from ScrapingHelpers import *
import HelperTools


	
# scrapy runspider MediapoolSpider.py -o Reports/Mediapool-30-Apr-2017.json -t json>Logs/output.txt
# runIt 2017-05-08

translateMonth={u'януари':'january',u'февруари':'february',u'март':'march',u'април':'april',u'май':'may',u'юни':'june',u'юли':'july',u'август':'august',u'септември':'september',u'октомври':'october',u'ноември':'november',u'декември':'december'}

'Get the today date'
today = date.today()
Today = today.strftime("%Y-%m-%d")

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
	
class MediapoolSpider(scrapy.Spider):
    name = "mediapool"
    #allowed_domains = ['mediapool.bg', 'www.mediapool.bg']
    allowed_domains = ['mediapool.bg']
    custom_settings = {
		'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def __init__(self):

		self.start_urls = ["http://mediapool.bg/today.html"]
		self.json_datafile = 'Mediapool/Reports/Mediapool-'+Today+'.json'
		self.links_seen = read_ids(self.json_datafile)
		print '-'*10,'Mediapool v(1.0)','-'*10

    def parse(self, response):
 
		links = response.xpath("//a[@class='news_in_a']/@href").extract()
		print "url: %s selected: %d" %(response.url, len(links))
		'take only the end of the Mediapool url. The number after the news string:'
		self.links_seen = map(lambda url: url.split('news')[1] , self.links_seen)

		for link in links:
			if link.split('news')[1] not in self.links_seen:
				yield scrapy.Request(url=link, callback=self.parse_page)

    def parse_page(self, response):
		url     = response.url
		title   = response.xpath('//div[@class="main_left"]/h1/text()').extract()[0].strip()
		article = ''.join(response.xpath('//div[@class="main_left"]/div/p/text()| //div[@class="main_left"]/div[@id="art_font_size"]/p/b/text() | //div[@class="main_left"]/div[@id="art_font_size"]/div/text()| //div[@class="main_left"]/div[@id="art_font_size"]/div/div/div/text() | //div[@class="main_left"]/div[@id="art_font_size"]/div/div/text()').extract()).strip() 

		pubDate=response.xpath('//div[@class="info wbig"]/text()').extract_first()
		if (pubDate[0:3] == ' | '):
			pubDate = pubDate[3:]
		#extract and prepare Article date
		(day, month, year)=pubDate.split('|')[1].split()
		month=HelperTools.bgMonthstoNumber(month)
		pubDate='%s.%s.%s'%(year,month,day)
		# dateParts=pubDate.split()
		# if (dateParts[0]=='|'):
			# dateParts=dateParts[1:]
		# trMonth=translateMonth[dateParts[3]]
		# articleDate= ('%s-%s-%s' %(dateParts[2],trMonth,dateParts[4])).lower()

		todaysDate=date.today().strftime("%Y.%m.%d")
		
		# Filter on todays date
		if (pubDate == todaysDate):
			yield {
				'url': url,
				'title': title,
				'text': article,
				'date': pubDate
			}	
