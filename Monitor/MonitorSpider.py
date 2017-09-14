# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import date, timedelta
import os.path
from scrapy.exceptions import CloseSpider
from sys import exit, path
import platform
if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 
from ScrapingHelpers import *
import HelperTools

'Get the today date'
today = date.today()
Today = today.strftime("%Y-%m-%d")

yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")

	
class MonitorSpider(scrapy.Spider):
    name = "Monitor"
    start_urls = ["http://www.monitor.bg/home/category/20",
	"http://www.monitor.bg/home/category/123",
	"http://www.monitor.bg/home/category/124",
	"http://www.monitor.bg/home/category/50",
	"http://www.monitor.bg/home/category/30",
	"http://www.monitor.bg/home/category/60",
	"http://www.monitor.bg/home/category/97",
	"http://www.monitor.bg/home/category/80",
	"http://www.monitor.bg/home/category/107",
	"http://www.monitor.bg/home/category/96",
    ]
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
		'CONCURRENT_REQUESTS_PER_DOMAIN':'1',
		'DOWNLOAD_DELAY':'5',
		'COOKIES_ENABLED':'False',
		# 'DEPTH_LIMIT':'3'

	}

	
    def __init__(self):

   		# "Empty output file"
        fileName="Monitor/Reports/Monitor-%s.json"%(Yesterday)
        f = open(fileName, 'w').close()

        print '-'*10,'Monitor v(2.0)','-'*10
        
    def parse(self, response):

        links=response.xpath('//div[@id="main"]/div[@class="row-fluid"]/div[@class="post clearfix"]')
        print "url: %s selected: %d" %(response.url, len(links))
        for link in links:
            url=link.xpath('div[@class="content"]/h2[@class="articleTitleHeader"]/a/@href').extract_first()
            pubDate=link.xpath('div[@class="meta"]/span[@class="pull-left"]/text()').extract()
            (day, month, year)=pubDate[1].split(',')[1].split()[0].split('-')
            pubDate = '%s.%s.%s' % (year, month, day)

            # fileter only yesterday records
            if (pubDate == yesterday.strftime("%Y.%m.%d")):
                url = response.urljoin(url)
                yield scrapy.Request(url=url, callback=self.parse_page)
                
		
    def parse_page(self, response):

        url = response.url
        
        
        title = response.xpath('//figure[@class="head-section"]/div[@class="head-section-content"]/h1/text()').extract_first()

        text =response.xpath('//div[@class="row-fluid"]/div[@class="content"]/h4/text() | '+
        '//div[@class="row-fluid"]/div[@class="content"]/div[@class="articleContentContainer"]/div/div/div/p/text() | '+
        '//div[@class="row-fluid"] /div[@class="content"]/div[@class="articleContentContainer"]/div/p/text() | '+
        '//div[@class="row-fluid"] /div[@class="content"]/div[@class="articleContentContainer"]/div/text() | '+
        '//div[@class="row-fluid"]/div[@class="content"]/div[@class="articleContentContainer"]/div/div/div/p/em/strong/text() | '+
        '//div[@class="row-fluid"] /div[@class="content"]/div[@class="articleContentContainer"]/div/div/p/text() | '+
        '//div[@class="row-fluid"] /div[@class="content"]/div[@class="articleContentContainer"]/div/div/div/div/p/text() | '+
        '//div[@class="row-fluid"] /div[@class="content"]/div[@class="articleContentContainer"]/div/pre/text()').extract()

        article=u''.join(text)
		
		# 'extract and prepare Article date'
        pubDate = response.xpath('//div[@class="row-fluid"]/figure[@class="head-section"]/div[@class="head-section-content"]/p[@class="meta"]/span/text()').extract_first()
        (day,month,year)=pubDate.strip().split()[1].split('-')
        articleDate='%s.%s.%s'%(year, month, day)

        print 'article date: %s  url: %s' %(articleDate,  url[0:url.find('-')]+' ... ')

        yield {
            'url': url,
            'title': title,
            'text': article,
            'date': articleDate
        }	

