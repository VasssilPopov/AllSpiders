import jsonlines
import os
# dates
from datetime import date, timedelta
def textHasData(line):
    return (line['text'] != "")

def getSetOfDates(fileName):
	dates = set()
	with jsonlines.open(fileName) as reader:
		for line in reader:
			dates.add(line['date'])

	listDates=list(dates)
	listDates.sort()
	return{'fileName':fileName,'dates':listDates}

def getRowCount(fileName):
    count = 0
    try:
        if os.path.isfile(fileName):
            with jsonlines.open(fileName) as reader:
                for line in reader:
                    count=count+1
    except:
        pass
    
    return count
   


'Get the Today adn Yesterday dates'
##Today = date.today().strftime("%Y-%m-%d")
##yesterday = date.today() - timedelta(1)
##Yesterday = yesterday.strftime("%Y-%m-%d")

today=date.today()
#today=date(2017,06,10)
Today = today.strftime("%Y-%m-%d")
yesterday = today - timedelta(1)
Yesterday = yesterday.strftime("%Y-%m-%d")

headings='%-15s %-12s %7s'%('Source','Date','Records')
recs=[{'Source':'Blitz','Date':Today,'Records':0},
    {'Source':'24chasa','Date':Today,'Records':0},
    {'Source':'Trud','Date':Today,'Records':0},
    {'Source':'Duma','Date':Today,'Records':0},
    {'Source':'Mediapool','Date':Today,'Records':0},
    {'Source':'ClubZ','Date':Today,'Records':0},
    {'Source':'Classa','Date':Today,'Records':0},
    {'Source':'Dnevnik','Date':Yesterday,'Records':0},
    {'Source':'Focus','Date':Yesterday,'Records':0},
    {'Source':'Monitor','Date':Yesterday,'Records':0},
    {'Source':'News','Date':Yesterday,'Records':0},
    {'Source':'OffNews','Date':Yesterday,'Records':0},
    {'Source':'PIK','Date':Yesterday,'Records':0},
    # {'Source':'SegaBG','Date':Yesterday,'Records':0}
     ]

line= '-'*36
print 'Daily Summary Report'
print 'Today: '+Today+'\n'+line
print headings+'\n'+line
for rec in recs:
    path=rec['Source']+'/Reports/'+rec['Source']+'-'+rec['Date']+'.json'
    rec['Records']= getRowCount(path)
    print '%-15s %-12s %7s'%(rec['Source'],rec['Date'],rec['Records'])
print line
