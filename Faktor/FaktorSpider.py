# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
import sys

# scrapy runspider FaktorSpider.py -o Reports/Faktor-2017-05-17.json -t jsonlines

'Get the yesterday date'
# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
TodayYear = today.strftime("%Y")
strToday = today.strftime("%Y.%m.%d")

def read_ids(file):

    'Read latest 11 chars from urls of the already processed publications '
    ids=set()

    try:
        with open(file, 'rb') as f:
            for item in json_lines.reader(f):
                ids.add(item["url"])
    except IOError:
        ids = set()

    return ids
def makeStdDate(day, monthName, year):

        months= {'jan':'01', 'feb':'02', 'mar':'03', 'apr':'04', 'may':'05', 'jun':'06', 'jul':'07', 'aug':'08', 'sep':'09', 'oct':'10', 'nov':'11', 'dec':'12'}
        dateExpr = '????.??.??'
        if (monthName in months):
                montNumber = months[monthName]
                dateExpr =  '%s.%s.%s' % (year,montNumber, day)

        return dateExpr
def getDate( response ):
        pubDate=u''.join(response.xpath('//article[@class="entry single"]/span[@class="entry-date"]/text()').extract()).strip()

        pubDate2 =  response.xpath('//article[@class="entry single"]/span[@class="entry-date"]/span/text()').extract()
        monthName=pubDate2[0][0:3].lower()

        months= {'jan':'01', 'feb':'02', 'mar':'03', 'apr':'04', 'may':'05', 'jun':'06', 'jul':'07', 'aug':'08', 'sep':'09', 'oct':'10', 'nov':'11', 'dec':'12'}
        dateExpr = '????.??.??'
        if (monthName in months):
                montNumber = months[monthName]
                dateExpr =  '%s.%s.%s' % (pubDate2[1],montNumber, pubDate)

        return dateExpr
class FaktorSpider(scrapy.Spider):
    name = "faktor.bg"
    allowed_domains = ['faktor.bg']
    start_urls = [
        "http://www.faktor.bg/bg/articles/novini", 
        "http://www.faktor.bg/bg/articles/politika",
        "http://www.faktor.bg/bg/articles/obshtestvo",
        "http://www.faktor.bg/bg/articles/ikonomika",
        "http://www.faktor.bg/bg/articles/kultura",
        "http://www.faktor.bg/bg/articles/layf-stayl",
        "http://www.faktor.bg/bg/articles/sport",
    ]
    
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'CONCURRENT_REQUESTS_PER_DOMAIN': '1',
        'DOWNLOAD_DELAY': '2',
        'COOKIES_ENABLED': 'False',
        }

    def __init__(self):
        # print '__init__'
        self.selectedCount = 0
        self.json_datafile = 'Faktor/Reports/Faktor-'+Today+'.json'
        self.links_seen = read_ids(self.json_datafile)
        'take only the end of the Mediapool url. The number after the news string:'
        #self.links_seen = set(map(lambda url: url.split('article/')[1] , self.links_seen))
        print '-'*10,'Faktor v(1.0)','-'*10
        print 'recorded articles: %d' % len(self.links_seen)
        
    def parse(self, response):
        if (self.selectedCount > 0):
            print 'added new articles: %s'% (str(self.selectedCount ))
        print '>>> New page <parse> url:', response.url
        self.selectedCount = 0

        #prepare index
        links = response.xpath('//article[@class="entry"]')
        items=[]
        
        for link in links:
        
            day = link.xpath('.//span[@class="entry-date"]/text()').extract_first().strip()
            month = link.xpath('//span[@class="entry-date"]/span/text()').extract_first().strip().lower()
            pubDate=makeStdDate(day, month, TodayYear)
            url=link.xpath('.//h2[@class="entry-title"]/a/@href').extract_first()
            
            items.append(tuple((pubDate, url)))
            
            # list of tuples sort it by date and time
        items_sorted_by_date = sorted(items, key=lambda tup: tup[0], reverse=True)
        
        for item in items_sorted_by_date:
        # extract date 
        # pubDate=link.xpath('.//p[@class="tinytext-novina"]/text()').extract_first()
        # articleDate = getStdDate(pubDate)
            articleDate=item[0]
            # print articleDate, articleDate == strToday

            # Filter on todays date
            if articleDate != strToday:
                return
            # url = item[1]
            url = response.urljoin(item[1])
            # print code, code not in self.links_seen
            if url not in self.links_seen:
                self.links_seen.add(url)
                # url = response.urljoin(url)
                # print 'to parse_details'
                self.selectedCount = self.selectedCount +1 
                yield scrapy.Request(url=url, callback=self.parse_details, meta={'articleDate':articleDate})

		# print "url: %s selected: %d" %( response.url, len(urls))
        
		# for url in urls:
		
			# if url not in self.links_seen:
				# self.links_seen.add(url)
                
                # url = response.urljoin(url)
                # yield scrapy.Request(url=url, callback=self.parse_details)

            ## follow pagination link
            # print 'follow pagination link'
            next_page_url=response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').extract_first()
            if next_page_url:
                next_page_url = response.urljoin(next_page_url)
                yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):

        # print 'parse_details'
        url     = response.url
        
        title = response.xpath('//div[@class="entry-media"]/h1/text()').extract_first()
        
        texts=response.xpath('//div[@class="entry-content"]/p/text() | //div[@class="entry-content"]/text() | //div[@class="entry-content"]/div/text() | //div[@class="entry-content"]/div/p/text()').extract()
 
        article = u' '.join(texts).strip()
        
		# pubDate = getDate(response)
		# # pubDate=response.xpath('//div[@id="page-left-content"]/div[@class="article"]/div[@class="head"]/span[@class="article-date"]/span/text()').extract_first()
		# # # 21.06.2017 10:59
		# (year, month, day)=pubDate.split('.')
		# articleDate='%s.%s.%s'%(year, month, day)
        articleDate = response.meta['articleDate']
        # print '>>1>> %s' % (articleDate)
		# articleDate=pubDate.split()[0]
		# print 'artDate: %s url= %s ' %(articleDate, url)
		# Filter on todays date
        # print '>>>>', articleDate, strToday, (articleDate == strToday), url
        if (articleDate == strToday):
            yield {
                'url': url,
                'title': title,
                'text': article,
                'date': articleDate
            }
