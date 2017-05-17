# -*- coding: utf-8 -*-
import json
from sys import exit
# import json_lines
import codecs 

json_data = []

def read_json(file):
	'Read the Json file in one of two possible formats'
	json_data = []

	with open(file) as f: # Check what is the first char of the file { or [
	    first_char = f.read(1)

	if first_char == '{': # Json Lines
		with open(file) as f:
			for line in f:
				json_data.append(json.loads(line))

	elif first_char == '[': # Json format
		with open(file) as f:
			json_data = json.load(f)	 		

	else:
		print "Can't determine the format of %",file

	f.close()		
	return json_data

def read_ids(file):

	'Read the urls of the already processed publications '

	ids=set()
	
	try:
		with open(file, 'rb') as f:
			for item in json_lines.reader(f):
				ids.add(item["url"])
	except IOError:
		ids = []
		# print 'error'

	return ids

def read_json_lines(file):

	'Read the urls of the already processed publications '

	ids=list()
	
	try:
		# with open(file, 'rb') as f:
			# for item in json_lines.reader(f):
				# ids.add(item)
				

		f = codecs.open(file, encoding='utf-8') 
		lines = f.readlines()
		f.close() 		

		for item in lines:
			ids.add(item)
				
				
	except IOError:
		ids = list()
		# print 'error'

	return ids

def list_urls(file):
	'List the urls of the retrieved publications'
	json_data = []
	json_data = read_json(file)
	
	for i in range(0,len(json_data)):
		print json_data[i]['url']

def check_empty(file):
	'Check if there are missing fields from the retrieved publications'
	json_data = []
	json_data = read_json(file)
	for i in range(0,len(json_data)):
		for key,val in json_data[i].items():
			if val == u"":
				print key,'is empty'
				print 'Url is:', json_data[i]['url']
				print 'Title is:', json_data[i]['title'].encode('utf-8')
	
	print "Check complete"				

def list_keywords(file, keywords):
	'List urls which contain certain keywords'
	json_data = []
	json_data = read_json(file)

	for keyword in keywords:
		print u'Urls for :',keyword.encode('utf-8')
		for line in json_data:
			if keyword in line['article']:
				print line['url']

