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
    months= {'яну':'01', 'фев':'02', 'мар':'03', 'апр':'04', 'май':'05', 'юни':'06', 'юли':'07', 'авг':'08', 'сеп':'09', 'окт':'10', u'ное':'11', u'дек':'12'}
    dateExpr = '????.??.??'
    if (monthName in months):
        montNumber = months[monthName]
        dateExpr =  '%s.%s.%s' % (str(year),montNumber, str(day))

    return dateExpr
# def getDate( response ):
        # pubDate=u''.join(response.xpath('//article[@class="entry single"]/span[@class="entry-date"]/text()').extract()).strip()

        # pubDate2 =  response.xpath('//article[@class="entry single"]/span[@class="entry-date"]/span/text()').extract()
        # monthName=pubDate2[0][0:3].lower()

        # months= {'яну':'01', 'фев':'02', 'мар':'03', 'апр':'04', 'май':'05', 'юни':'06', 'юли':'07', 'авг':'08', 'сеп':'09', 'окт':'10', 'ное':'11', 'дек':'12'}
        # dateExpr = '????.??.??'
        # if (monthName in months):
                # montNumber = months[monthName]
                # dateExpr =  '%s.%s.%s' % (pubDate2[1],montNumber, pubDate)

        # return dateExpr
class DnesSpider(scrapy.Spider):
    name = "dnes"
    allowed_domains = ['dnes.bg']
    start_urls = [
        "https://www.dnes.bg/news.php?today", 
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
        self.json_datafile = 'Dnes/Reports/Dnes-'+Today+'.json'
        self.links_seen = read_ids(self.json_datafile)
        'take only the end of the Mediapool url. The number after the news string:'
        #self.links_seen = set(map(lambda url: url.split('article/')[1] , self.links_seen))
        print '-'*10,'Dnes v(1.0)','-'*10
        print 'recorded articles: %d' % len(self.links_seen)
        
    def parse(self, response):
        if (self.selectedCount > 0):
            print 'added new articles: %s'% (str(self.selectedCount ))
        print '>>> New page <parse> url:', response.url
        self.selectedCount = 0

        #prepare index
        urls = response.xpath('//div[@class="b2"]/div[@class="ttl"]/a/@href').extract()

        for url in urls:
            
            print "url: %s selected: %d" %( response.url, len(urls))
            
            if url not in self.links_seen:
                self.links_seen.add(url)
                
                url = response.urljoin(url)
                yield scrapy.Request(url=url, callback=self.parse_details)

        # follow pagination link
        next_page_url=response.xpath('//p[@class="pages"]/a[@class="pagination-next"]/@href').extract_first()
        print 'follow pagination link: %s' % (next_page_url)
       
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):

        # print 'parse_details'
        url     = response.url

        title=response.xpath('//div[@id="art_header"]/h1[@class="title"]/text()').extract_first()
        
        texts=response.xpath('//div[@id="art_start"]/p/text() | //div[@id="art_start"]/div/text()').extract()
        article = u''.join(texts)
        
        date=response.xpath('//div[@class="art_author"]/text()').extract_first()
        (day, month, year)=date.split()[0:3]
        #print day, type(month), year
        articleDate=makeStdDate(day, month, year)
        # print '>1>',articleDate, strToday,(articleDate == strToday)
        # if (articleDate == strToday):
        yield {
            'url': url,
            'title': title,
            'text': article,
            'date': strToday  #articleDate
        }
