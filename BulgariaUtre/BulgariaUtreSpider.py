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
    print file
    try:
        with open(file, 'rb') as f:
            for item in json_lines.reader(f):
                ids.add(item["url"])
    except IOError:
        ids = set()

    return ids

def urlGetDate(url):
    pubDate=url.split('.bg/')[1][0:10].replace('/','.')
    return pubDate

def urlGetID(url):
    id=url.split('.bg/')[1][11:20].split('-')[0]
    return id

def makeStdDate(day, monthName, year):
    months= {'яну':'01', 'фев':'02', 'мар':'03', 'апр':'04', 'май':'05', 'юни':'06', 'юли':'07', 'авг':'08', 'сеп':'09', 'окт':'10', u'ное':'11', u'дек':'12'}
    dateExpr = '????.??.??'
    if (monthName[0:3] in months):
        montNumber = months[monthName[0:3]]
        dateExpr =  '%s.%s.%s' % (str(year),montNumber, str(day))

    return dateExpr

class BulgariaUtreSpider(scrapy.Spider):
    name = "BulgariaUtre"
    allowed_domains = ['bulgaria.utre.bg']
    start_urls = [
        "http://www.bulgaria.utre.bg/news/", 
    ]
    
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'CONCURRENT_REQUESTS_PER_DOMAIN': '1',
        # 'DOWNLOAD_DELAY': '2',
        'COOKIES_ENABLED': 'False',
        }

    def __init__(self):
        # print '__init__'
        self.selectedCount = 0
        self.json_datafile = 'BulgariaUtre/Reports/BulgariaUtre-'+Today+'.json'
        self.links_seen = read_ids(self.json_datafile)
        'take only the end of the Mediapool url. The number after the news string:'
        self.links_seen = set(map(lambda url: urlGetID(url) , self.links_seen))
        print '-'*10,'BulgariaUtre v(1.0)','-'*10
        print 'recorded articles: %d' % len(self.links_seen)
        return 
    def parse(self, response):
        if (self.selectedCount > 0):
            print 'added new articles: %s'% (str(self.selectedCount ))
        print '>>> New page <parse> url:', response.url
        self.selectedCount = 0

        #prepare index
        # urls = response.xpath('//div[@class="b2"]/div[@class="ttl"]/a/@href').extract()
        urls=response.xpath('//div[@class="three-col last-col"]/a[@class="f16 title"]/@href').extract()
        for url in urls:
            curDate='%s.%s.%s' % tuple(url.split('bg/')[1].split('/')[0:3])
            if curDate != strToday:
                return
            idURL = urlGetID(url)
            if idURL not in self.links_seen:
                print 'added: ', idURL, len(self.links_seen), url
                self.links_seen.add(idURL)

                # url = response.urljoin(url)
                yield scrapy.Request(url=url, callback=self.parse_details)

        # follow pagination link
        # next_page_url=response.xpath('//p[@class="pages"]/a[@class="pagination-next"]/@href').extract_first()
        # print 'follow pagination link: %s' % (next_page_url)
        next_page_url= response.xpath('//ul[@class="pagination"]/li[last()]/a[@class="navigation"]/@href').extract_first()
        print 'Next Page url: %s' % next_page_url
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):

        print 'parse_details'
        url     = response.url

        # title=response.xpath('//div[@id="art_header"]/h1[@class="title"]/text()').extract_first()
        title=response.xpath('//div[@class="article"]/h1[@class="title f24"]/text()').extract_first()
        
        # texts=response.xpath('//div[@id="art_start"]/p/text() | //div[@id="art_start"]/div/text()').extract()
        # article = u''.join(texts)
        
        texts=response.xpath('//div[@class="text f13 dev"]/p/text()').extract()
        article=u' '.join(texts)


        # date=response.xpath('//div[@class="art_author"]/text()').extract_first()
        # (day, month, year)=date.split()[0:3]
        
        pubDate=response.xpath('//div[@class="left date f12"]/text()').extract_first()
        (day,month, year)=pubDate.split('|')[-2].split(',')[-2].split()
        
        #print day, type(month), year
        articleDate=makeStdDate(day, month, year)
        print articleDate, strToday,articleDate == strToday
        if (articleDate == strToday):
            yield {
                'url': url,
                'title': title,
                'text': article,
                'date': strToday  #articleDate
            }
