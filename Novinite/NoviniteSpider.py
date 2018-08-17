# -*- coding: utf-8 -*-
import scrapy
import os
from datetime import date, timedelta
import os.path


yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
yesterdaysDate = yesterday.strftime("%Y.%m.%d")
BGMonths={u'януари':'01',u'февруари':'02',u'март':'03',u'април':'04',u'май':'05',u'юни':'06',u'юли':'07',u'август':'08',u'септември':'09',u'октомври':'10',u'ноември':'11',u'декември':'12'}

class NoviniteSpider(scrapy.Spider):
    name = "novinite"
    start_urls=[
    'http://www.novinite.bg/archives/'+Yesterday,
    ]
    count = 0
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    def __init__(self):
        print '-'*10,'Novinite v(1.0)','-'*10
        
        # zeroes the file
        fileName="Novinite/Reports/Novinite-%s.json"%(Yesterday)
        if (os.path.exists(fileName) and os.path.getsize(fileName) > 0):
                f = open(fileName, 'w').close()

    def parse(self, response):
    
        print 'Page url %s' % (response.url)
        # zeroes the file
#        # print '>*> ',fileName, (os.path.exists(fileName) and os.path.getsize(fileName) > 0)
        
#        if (os.path.exists(fileName) and os.path.getsize(fileName) > 0):
#            f = open(fileName, 'w').close()

        # urls=response.xpath('//article[@class="secondary-article-v2 border-top list-item"]/div[@class="text"]/h2/a/@href').extract()
        urls=response.xpath('//div[@class="news_list"]/div[@class="item"]/h2/a/@href').extract()
        print len(urls),' urls collected'
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_page)
        
    def parse_page(self, response):
        url = response.url
        title=response.xpath('//div[@id="content"]/h1/text()').extract_first()
        texts=response.xpath('//div[@id="textsize"]/p/text() | //div[@id="textsize"]/p/b/text() | //div[@id="textsize"]/div/div/text() | //div[@id="textsize"]/div[@class="article-text"]/p/text() | //div[@id="textsize"]/div/p/text() | //div[@id="textsize"]/p/span/text() | //div[@id="textsize"]/div/text() | //div[@id="textsize"]/p/span/span/text()  | //div[@class="text-wrapper"]/div[@class="article-text-inner-wrapper io-article-body"]/text()').extract()
        article=u''.join(texts)

        # 'extract and prepare Article date'
        data=response.xpath('//div[@class="newsdate"]/span/text()').extract_first()
        (day, month, year)=data.split(',')[0].split()
        articleDate = '%s.%s.%s' % (year,BGMonths[month],str(day).zfill(2))
        
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
