# -*- coding: utf-8 -*-
import scrapy
import logging
import json
from sys import exit, path
from datetime import date, timedelta
import urllib
import platform

if platform.system() == 'Linux':
	path.append('/home/peio/dev/AllSpiders/_LIBRARY/')
elif platform.system() == 'Windows':
	path.append('C:\STUDY_SPIDERS\_AllSpiders\_LIBRARY')
else: 
	print 'Unknown platform' 
	exit() 

from ScrapingHelpers import *

# scrapy runspider PIKSpider.py -o PIK-2017-05-17.json -t jsonlines
# RunIt 2017-05-17

'Get the yesterday date'
yesterday = date.today() - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")
today = date.today()
Today = today.strftime("%Y-%m-%d")
Today = (date.today()).strftime("%Y-%m-%d")


class PIKSpider(scrapy.Spider):
	name = 'PIK'
	allowed_domains = ['pik.bg']

	start_urls = [
		"http://pik.bg/политика-cat6.html"

    ]
	custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

	def __init__(self):

		print '-1- __init__ --'
		self.urls = ["http://pik.bg/политика-cat6.html"]
		
		self.json_datafile = 'Reports/PIK-'+Yesterday+'.json'
		print "Output file name: %s" %(self.json_datafile)
		
		self.links_seen=[]
		self.links_seen = self.get_ids(self.json_datafile)
		print '>> Links seen:%d >> '%(len(self.links_seen))
		
		# for ll in self.links_seen:
			# print ll.decode("utf-8"), sys.defaultencoding()
			# print '------------------------------------------'
			# print type(ll)


		self.pubTime=''
		self.cnt=0
		
	# def read_ids(file):
	def read_urls(self, file):
		# print	'>>> Read the urls of the already processed publications '
		json_data = []
		json_data = read_json(file)
		ids = []
		for i in range(0,len(json_data)):
			d = json_data[i]['url']
			d2=urllib.unquote_plus(urllib.unquote_plus(d))
			# d2=unicode(d2,'utf-8')



			# d=urllib.unquote(urllib.unquote(d))
			#d=urllib.unquote(urllib.unquote(d))
			# d=unicode(d,'utf-8')


			ids.append(d2)
		return ids
		
		
	def get_ids(self, json_datafile):

		print '-2- get_ids -- local -- it returns set'
		ids = []
		try:
			ids = self.read_urls(json_datafile)
		except Exception, e:
			print '-2.1- get_ids -- local -- Error:'
			print e			
			return set(ids)
			
		return set(ids)

	def start_requests(self):
	
		print '-3- start_requests --'
		for url in self.urls:
			yield scrapy.Request(url=url, callback=self.parse)    

	def parse(self, response):
	
		print '-4- start parse --'
		# 'We need the titles, links and times to index and follow'
		
		links=response.xpath('//div[@class="right_part"]/a/@href').extract()

		# links=links[:todayArticles]
		
		# print type(self.links_seen)
				
		# Както и механизъм за проследяване на следваща страница
		for link in links:
			# print type(link)
			# print link
			# print (link in self.links_seen)
			# print (link in self.links_seen)
			# print link
			if not (link in self.links_seen):
				self.cnt = self.cnt+1
				print '-4.5- parse -- write down record %d'%(self.cnt)
				yield scrapy.Request(url=link, callback=self.parse_page)
		print '-4.9- parse -- Finish'


	def parse_page(self, response):

		url     = response.url
		title = response.xpath('//*[@id="hdscrolll"]/div/text()').extract_first()
		
		art_alternatives = {}
		art_alternatives[0] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/text()|//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/a/span/strong/text()').extract()
		art_alternatives[1] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/p/span/text()').extract()
		art_alternatives[2] = response.xpath('//*[@id="content"]/div[@class="item left first"]/div[@class="text2"]/div[@class="lead"]/p/text()').extract()

		for key in art_alternatives:
			art_alternatives[key] = list( map   ( lambda str: str.strip(), art_alternatives[key] ) )
			art_alternatives[key] = list( filter( lambda str: str != u'' , art_alternatives[key] ) )
			art_alternatives[key] = ' '.join(art_alternatives[key])

		art_alternatives = list( filter( lambda str: str != u'' , art_alternatives.values() ) )	

		# assert len(art_alternatives) == 1, 'Issue with %s'%url		

		article=' '.join(art_alternatives)
		
		(day,month,year) = response.css('time.left::text').extract()[0].split('|')[1].split('.')
		time = year+"-"+month+"-"+day

		self.cnt=self.cnt+1
		# print '-5- saved - %s -'%(self.cnt)
		
		# print "url: %s" %(url)
		# print "title: %s" %(title)
		# print "time: %s" %(self.pubTime)
		# print "article: %s)"%(article)
		yield {
			'url': url,
			'title': title,
			'text': article,
			'time': time

		}	
