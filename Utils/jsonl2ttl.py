#!/usr/bin/env python
# encoding: utf-8

# Convert jsonlines files to turtle syntax (.ttl) in order to load them in GraphDB

import jsonlines
import glob
from sys import exit
from rdflib import Namespace, URIRef, Graph, Literal
from rdflib.namespace import RDF, DC



# print( glob.glob("AllSpiders\Dnevnik\Reports\*.json") )

exit()

# g = Graph()

sites = ["24chasa", "Actualno", "BgOnAir", "Blitz", "BNews", "Classa", "ClubZ", "Dnes", "Duma", "Epicenter", "Faktor", "Mediapool", "StandartNews", "Trud", "Cross", "Dnevnik", "Focus", "Monitor", "News", "Novinite", "OffNews", "PIK"] 

for site in sites: 
  g = Graph()
  print site
  for news in glob.glob("AllSpiders\\"+site+"\Reports\*.json"):

    with jsonlines.open(news) as reader:
      for obj in reader:
        # print obj['title'].replace("\n", '').encode('utf-8')
        # print obj['date']
        g.add( (URIRef(obj['url']), RDF.type , Literal(obj['title']) ) )
        g.add( (URIRef(obj['url']), RDF.type , Literal(obj['text']) ) )
        # g.add( (URIRef(obj['url']), DC.title , obj['title'] ) )
        # g.add( (URIRef(obj['url']), DC.date , obj['date']) )


  g.serialize(destination=site+'.ttl', format='turtle')

