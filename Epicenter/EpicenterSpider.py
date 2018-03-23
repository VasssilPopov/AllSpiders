#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
from datetime import date, timedelta
import json
import json_lines
from scrapy.exceptions import CloseSpider
import os
import sys

# scrapy runspider 24chasaSpider.py -o Reports/24chasa-2017-05-17.json -t jsonlines
# RunIt 2017-05-17

# yesterday = date.today() - timedelta(1)
# Yesterday = yesterday.strftime("%Y-%m-%d")

today = date.today()
Today = today.strftime('%Y-%m-%d')
strToday = today.strftime('%Y.%m.%d')

def read_ids(file):
    '''Read latest 11 chars from urls of the already processed publications '''

    ids = set()

    try:
        with open(file, 'rb') as f:
            for item in json_lines.reader(f):
                ids.add(item['url'])
    except IOError:
        ids = set()

    # print 'error'

    return ids

# def getStdDateOLD(dateString):

    # months ={u'ян.':'01', u'февр.':'02', u'март':'03', u'апр.':'04', u'май':'05', u'юни':'06',
          # u'юли':'07', u'авг.':'08', u'септ.':'09', u'окт.':'10', u'ноем.':'11', u'дек.':'12'}
    # print 'dateString:%s ' % (dateString)
    # (day,month, year)=dateString.split('|')[-2].strip().split(' ')
    # dateExpr='????.??.??'

    # if (month in months):
        # month = months[month]
        # dateExpr =  '%s.%s.%s' % (year, month, ('00'+day)[-2:])

    # return dateExpr    

def getStdDate(dateString):
    months ={u'ян.':'01', u'февр.':'02', u'март':'03', u'апр.':'04', u'май':'05', u'юни':'06',
          u'юли':'07', u'авг.':'08', u'септ.':'09', u'окт.':'10', u'ноем.':'11', u'дек.':'12'}
    #print 'dateString:%s ' % (dateString)
    (day,month, year)=dateString.split('|')[-2].strip().split(' ')
    dateExpr='????.??.??'
    timeValue=dateString.split('|')[-1].strip()    	
    if (month in months):
        month = months[month]
        dateExpr =  '%s.%s.%s_%s' % (year, month, ('00'+day)[-2:],timeValue)

    return dateExpr    
    
    
class EpicenterSpider(scrapy.Spider):
    name = 'epicenter'
    allowed_domains = ['epicenter.bg']
    start_urls = [
        'http://epicenter.bg/category/bulgaria/2/1',
        'http://epicenter.bg/category/law/3/1',
        'http://epicenter.bg/category/business/4/1',
        'http://epicenter.bg/category/obstestvo/11/1',
        'http://epicenter.bg/category/culture/6/1',
        'http://epicenter.bg/category/world/7/1',
        'http://epicenter.bg/category/sport/8/1',
        'http://epicenter.bg/category/weekend/10/1',
        'http://epicenter.bg/category/recipes/9/1',
        ]
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        'CONCURRENT_REQUESTS_PER_DOMAIN': '1',
        'DOWNLOAD_DELAY': '2',
        'COOKIES_ENABLED': 'False',
        # 'DEPTH_LIMIT':'4'
        }


    def __init__(self):

        print '__init__'
        self.selectedCount = 0
        self.json_datafile = 'Epicenter/Reports/Epicenter-' + Today + '.json'
        self.links_seen = read_ids(self.json_datafile)
        
        self.links_seen = set(map(lambda url: url.split('/')[-3],
                              self.links_seen))
                              
        print '-' * 10, 'Epicenter v(1.0)', '-' * 10
        # print self.links_seen
        print 'recorded articles: %d' % len(self.links_seen)


    def parse(self, response):
    
        if (self.selectedCount > 0):
            print 'added new articles: %s'% (str(self.selectedCount ))
        self.selectedCount = 0
        print '>>> New page <parse> url:', response.url
        links = response.xpath('//td[@class="products_list"]/a')
        #print '>Count links: ',len(links)
        items=[]
        for link in links:
            vDate=link.xpath('.//p[@class="tinytext-novina"]/text()').extract_first()
            vDate=getStdDate(vDate)
            vUrl = link.xpath('@href').extract_first()
            items.append( tuple([vDate, vUrl]))
        # list of tuples sort it by date and time
        items_sorted_by_date = sorted(items, key=lambda tup: tup[0], reverse=True)
        # for itm in items_sorted_by_date:
            # print itm[0]
        # urls = response.xpath('//tr/td[@class="products_list"]/a/@href').extract()
        #links = response.xpath('//td[@class="products_list"]/a')
        for item in items_sorted_by_date:
            # extract date 
            # pubDate=link.xpath('.//p[@class="tinytext-novina"]/text()').extract_first()
            # articleDate = getStdDate(pubDate)
            articleDate=item[0][0:-6]

            # Filter on todays date
            if articleDate != strToday:
                return
            # print 'Selected article date: %s , url:%s' % (articleDate,item[1])
            #url=link.xpath('@href').extract_first()
            url=item[1]
            code=url.split('/')[-3]
            # print code, code not in self.links_seen
            if code not in self.links_seen:
                self.links_seen.add(code)
                url = response.urljoin(url)
                # print 'to parse_details'
                self.selectedCount = self.selectedCount +1 
                yield scrapy.Request(url=url, callback=self.parse_details, meta={'articleDate':articleDate})

        # follow pagination link
        next_page_url=response.xpath('//div[@class="pagination"]/a[last()]/@href').extract_first()
        next_page_url = response.urljoin(next_page_url)
        if next_page_url:
            # print 'NEXT PAGE url: %s' % next_page_url
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):

        # print 'parse_details'

        url = response.url
        
        title=response.xpath('//tr/td/h1/text()').extract_first()
        
        texts=response.xpath('//tr/td/p[@class="description_b"]/text() | //div[@id="adjuster"]/p/text() | //div[@id="adjuster"]/div/text()  | //div[@id="anons"]/text() | //div[@id="content-main"]/article/div/p/text() | //div[@id="content-main"]/article/div/p/strong/text() | //div[@id="adjuster"]/p/span/text()').extract()
        article=u' '.join(texts)
        
        # pubDate=response.xpath('//tr/td/div/p[@class="tinytext-novina"]/text()').extract_first()
        # articleDate = getStdDate(pubDate)

        yield {
            'url': url,
            'title': title,
            'text': article,
            # 'date':  articleDate[0:-6],
            'date': response.meta['articleDate']
            }
