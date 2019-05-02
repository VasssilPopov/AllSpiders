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
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y.%m.%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
strToday = today.strftime("%Y.%m.%d")
#yesterday = (date.today() - timedelta(1)).strftime("%Y.%m.%d")


def read_ids(file):

#    'Read latest 6 chars from urls of the already processed publications '

    ids=set()

    try:
        with open(file, 'rb') as f:
            for item in json_lines.reader(f):
                ids.add(item["url"][-6:])
    except IOError:
        ids = set()
    # print 'error'

    return ids

# def translateDateBG_EN(strDate):

    # monthsBG_EN={u'януари':u'january',u'февруари':u'february',u'март':u'march',u'април':u'april',u'май':u'may',u'юни':u'june',u'юли':u'july',u'август':u'august',u'септември':u'september',u'октомври':u'october',u'ноември':u'november',u'декември':u'december'}

    # dateParts=strDate.split()
    # v=dateParts[1].lower()
    # dateParts[1] = monthsBG_EN[v]
    # result = ' '.join(dateParts[:3])
    # return result

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
        "https://duma.bg/?go=newspaper&p=list",
        # "https://duma.bg/?go=news&p=list&categoryId=1",
        # "https://duma.bg/?go=news&p=list&categoryId=2",
        # "https://duma.bg/?go=news&p=list&categoryId=3",
        # "https://duma.bg/?go=news&p=list&categoryId=4",
        # "https://duma.bg/?go=news&p=list&categoryId=5",
        # "https://duma.bg/?go=news&p=list&categoryId=6",
        # "https://duma.bg/?go=news&p=list&categoryId=7",
    ]
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
        # 'CONCURRENT_REQUESTS_PER_DOMAIN':'1',
#		'DOWNLOAD_DELAY':'3',
        'COOKIES_ENABLED':'False',
#        'DEPTH_LIMIT':'2'
    }
    
    def __init__(self):
    
        self.json_datafile = 'Duma/Reports/Duma-'+Today+'.json'
        self.links_seen = read_ids(self.json_datafile)
        'take only the end of the Mediapool url. The number after the news string:'

        # self.links_seen = map(lambda url: url.split('node/')[1] , self.links_seen)
        print '-'*10,'Duma v(1.0)','-'*10
        print 'seen: %d'% (len(self.links_seen))
        
    def parse(self, response):
        
        #links=response.xpath("//section/div/div/div[@class='news_list_hdr/div/h3/a/@href']")
        
        links=response.xpath("//section/div/div/div[@class='news_list_hdr']/div")
        
        print "url: %s selected: %d" %(response.url, len(links))
        for link in links:
        
            #<old>date_issue = link.xpath('.//span[@class="views-field-field-issue-date-value"]/span[@class="field-content"]/span/text()').extract_first()
            ##date_issue=link.xpath("./div/p/time/@datetime").extract_first()
            date_issue= link.xpath("./p[@class='date']/time/@datetime").extract_first()
            #dateYesterday = convertDate(date_issue)
            date_issue = str(date_issue)[:10]
            
            dateYesterday = date_issue.replace('-','.')
            #print ">>>",dateYesterday == strToday,dateYesterday, strToday
            url = link.xpath("./h3[@class='cap']/a/@href").extract_first()
            #print url

            if (dateYesterday != strToday):
                return
            ##url = link.xpath('.//div/h3[@class="cap"]/a/@href').extract_first()
            url = link.xpath("./h3[@class='cap']/a/@href").extract_first()
            #print url
             #<old>code=url.split('node/')[1]
            code = url[-6:]
            if code not in self.links_seen:
                print "add code: "+code
                self.links_seen.add(code)
                urlTemp = response.urljoin(url)
                yield scrapy.Request(url=urlTemp, callback=self.parse_details)
        print ' follow pagination link'
        # follow pagination link
        #<old>next_page_url= response.xpath('//div[@class="item-list"]/ul[@class="pager"]/li[@class="pager-next"]/a[@class="active"]/@href').extract_first()
        next_page_url= response.xpath("//div[@class='wrp_pagination']/ul/li/a[@class='next']/@href").extract_first()
        #print 'Next Page URL: %s' % (next_page_url)
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            print 'Next Page URL: %s' % (next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):

        url     = response.url
        #print url
       #old>title = response.xpath('//div[@class="container"]/p[@class="title"]/a/text()').extract_first()
        title = response.xpath("//div[@id='newsDtlImgCap']/h1[@class='cap']/text() | //div/div[@class='news_dtl_hdr']/h1[@class='cap']/text()").extract_first()

        #<old>text = response.xpath('//div[@class="container"]/div[@class="meta"]/div[@class="content"]/p/text() | //div[@class="container"]/div[@class="meta"]/div[@class="content"]/p/strong/text()').extract()
        text = response.xpath("//div[@id='newsDtl_Body']/p/text()").extract()
        article = u' '.join(text)
        #print article[:10]
        #<old>bDate =response.xpath('//div[@class="container"]/div[@class="meta"]/span[@class="date-display-single"]/text()').extract_first()
        pubDate = response.xpath("//div[@id='newsDtlImgCap']/div/p[@class='date']/time/@datetime | //div[@class='news_dtl_hdr']/div/p/time/@datetime").extract_first()
        #'2018-11-14 15:38:00'
        tmp = pubDate[:10]
        pubDate = tmp.replace('-','.')
        # 2018.11.13
        #print "SAVE"
        #<old>pubDate=convertDate(pubDate)
        # print 'artDate: %s url= %s ' %(articleDate, url)
        # Filter on todays date
        # print pubDate, strToday, (pubDate == strToday), url
        # if (pubDate == strToday):
        yield {
            'url': url,
            'title': title,
            'text': article,
            'date': pubDate
        }

