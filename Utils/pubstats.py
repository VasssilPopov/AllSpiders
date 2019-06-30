#!/usr/bin/env python
# encoding: utf-8

# Generate publications stats for the purposes of quality monitoring

from sys import exit
import datetime
import glob
import jsonlines

#print( glob.glob("../Dnevnik/Reports/*.json") )

#exit()

sites = ["24chasa", "Actualno", "BgOnAir", "Blitz", "BNews", "Classa", "ClubZ", "Dnes", "Duma", "Epicenter", "Faktor", "Mediapool", "StandartNews", "Trud", "Cross", "Dnevnik", "Focus", "Monitor", "News", "Novinite", "OffNews", "PIK"] 
#sites = ["Dnevnik"]

for site in sites: 
  print site
  for news in glob.glob("../"+site+"/Reports/*.json"):

    with jsonlines.open(news) as reader:
      # Publications per day
      publications = 0
      total_symbols = 0
      for obj in reader:
        publications +=1
        total_symbols += len(obj["text"])

        datesplit =  obj["date"].split(".")
        # Monday is 1 and Sunday is 7.
        DayOfWeek = datetime.date(int(datesplit[0]),int(datesplit[1].lstrip("0")),int(datesplit[2].lstrip("0"))).isoweekday()
        
        # print publications,obj['date'],len(obj["text"]),obj['title'].encode('utf-8')
    
    # date, publications, total_symbols
    print site,"\t",datesplit[0]+"-"+datesplit[1]+"-"+datesplit[2],"\t",DayOfWeek,"\t",publications,"\t",total_symbols            

