import scrapy
import logging
import json
from sys import exit, path
# path.append('/home/peio/dev/Scrapy')
path.append('C:\STUDY_SPIDERS\Work\Spiders\_LIBRARY')
from ScrapingHelpers import *
from datetime import date, timedelta
# from scrapy.selector import HtmlXPathSelector

# '$ scrapy crawl Dnevnik -o Dnevnik.json -t jsonlines'
# scrapy runspider BlitzSpider.py -o Blitz-03-May-2017.json -t json

'Get the yesterday date'
# yesterday = date.today() - timedelta(1)
today = date.today()
# Today = today.strftime("%d-%b-%Y")
Today = "2017-05-05"

class focusNews2Spider(scrapy.Spider):
    name = "focusNews2"
    allowed_domains = ["focus-news.net"]
    start_urls = [
        "http://focus-news.net/news/Yesterday/",
    ]
	# def __init__(self):
		# self.urls = ["http://www.blitz.bg/politika",
		# "http://www.blitz.bg/obshtestvo",
		# "http://www.blitz.bg/obshtestvo/regioni"]
		# self.json_datafile = 'Focus-'+Today+'.json'
		# self.links_seen = self.get_ids(self.json_datafile)
	def get_ids(self, json_datafile):
		ids = []
			
		try:
			ids = read_ids(json_datafile)
		except (IOError,ValueError):
			return set(ids)

		return set(ids)
	
	
	
	
    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
            # f.write(response.body)
			
		self.json_datafile = 'Focus-'+Today+'.json'
		self.links_seen = self.get_ids(self.json_datafile)

		#'We need the titles, links and times to index and follow'

		titles = response.css('a.cnk-title::text').extract()
		titles = list( map (lambda str: str.strip(), titles) )
		
		i=0
		
		try:
			for title in titles:
				print title
				i =i + 1
		except:
			print i
			i =i + 1
		links  = response.css('a.cnk-title::attr(href)').extract()
		links  = list( map(lambda str:'http://focus-news.net/'+str[2:], links) )
		

		times  = response.css('span.date::text').extract()
		times  = list( map(lambda str:str.split('|')[0], times) )
		
	
		for link in links:
			if link not in self.links_seen:
				# yield scrapy.Request(url=link, callback=self.parse_page)
				self.logger.info('Calling follow on %s', link)
				


				
