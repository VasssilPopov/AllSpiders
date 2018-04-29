# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import date, timedelta
import os.path


yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
yesterdaysDate = yesterday.strftime("%Y.%m.%d")
BGMonths={u'януари':'01',u'февруари':'02',u'март':'03',u'април':'04',u'май':'05',u'юни':'06',u'юли':'07',u'август':'08',u'септември':'09',u'октомври':'10',u'ноември':'11',u'декември':'12'}

class ActualnoSpider(scrapy.Spider):
    name = "bnews"
    start_urls=[
    "http://www.bnews.bg/news/yesterday",
    ]
    count = 0
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
        }
    def __init__(self):
        print '-'*10,'BNews v(1.0)','-'*10
        
        # zeroes the file
        fileName="BNews/Reports/BNews-%s.json"%(Yesterday)
        if (os.path.exists(fileName) and os.path.getsize(fileName) > 0):
                f = open(fileName, 'w').close()

    def parse(self, response):
    
        print 'Page url %s' % (response.url)
        
        # # zeroes the file
        # fileName="Bnews/Reports/Bnews-%s.json"%(Yesterday)
        # if (os.path.exists(fileName) and os.path.getsize(fileName) > 0):
            # f = open(fileName, 'w').close()
        # urls=response.xpath('//article[@class="secondary-article-v2 border-top list-item"]/div[@class="text"]/h2/a/@href').extract()
        
        
        urls = response.xpath('//div[@class="pull-left details"]/h4/a/@href').extract()

        print len(urls),' urls collected'
        
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_page)
        
        next_page_url = response.xpath('//ul[@id="yw0"]/li[@class="next"]/a/@href').extract_first()
        if next_page_url:
            next_page_url=response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        
        
        # tmp_url=response.xpath('//div[@class="content"]/div[@class="tab"]/div[@class="pagginator"]/a')[-1]
        # p = tmp_url.xpath('.//text()').extract_first()[-2:]
        # self.logger.warning('NEW PAGE: ',p)
        
        # if p == u'>>':
            # next_page_url=tmp_url.xpath('.//@href').extract_first()
            # next_page_url=response.urljoin(next_page_url)
            # print 'will follow next page: %s' % (next_page_url)
            # yield scrapy.Request(url=next_page_url, callback=self.parse)
            
    def parse_page(self, response):

        url = response.url
        #title=response.xpath('//article[@id="article-content"]/h1/text()').extract_first()
        title=response.xpath('//div[@id="article-content"]/h3[@class="title"]/text()').extract_first()
        #texts=response.xpath('//div[@id="article-text"]/p/text() | //div[@id="article-text"]/text()').extract()
        texts=response.xpath('//div[@id="article-text"]/p/text() | //div[@id="article-text"]/text() | //div[@id="article-text"]/div/text() | //div[@id="article-text"]/div/p/text()').extract()
        article=u' '.join(texts)

        # 'extract and prepare Article date'
        # time=response.xpath('//div[@class="info"]/time/text()').extract_first().strip()
        # (day, month,year)=time.split()[0].split('.')
        
        # articleDate = '%s.%s.%s' % (year,month,day)
        pubDate=response.xpath('//div[@id="article-content"]/p[@class="date"]/text()').extract_first()
        (day, month, year) = pubDate.split(',')[-2].split()
        month=BGMonths[month.lower()]
        articleDate = '%s.%s.%s' % (year,month,day)
        self.count = self.count + 1
        print '\t', self.count, articleDate,(articleDate == yesterdaysDate),url
        # Filter on todays date
        if (articleDate == yesterdaysDate):
            yield {
                'url': url,
                'title': title,
                'text': article,
                'date': articleDate
            }    
