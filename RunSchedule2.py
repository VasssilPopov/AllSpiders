# -*- coding: utf-8 -*-

from os import system

import schedule
import time

def jobYesterday():
    print("Starts at "+str(time.ctime()))
    system('Python RunYesterdaySpiders.py')
    print("Ends at "+str(time.ctime()))

def jobToday():
    print("Starts at "+str(time.ctime()))
    system('Python RunTodaySpiders.py')
    print("Ends at "+str(time.ctime()))

def jobDuma():
    print("Starts at "+str(time.ctime()))
    system('Python RunDumaSpider.py')
    print("Ends at "+str(time.ctime()))

#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("15:00").do(jobDuma)
schedule.every().day.at("01:00").do(jobYesterday)
#schedule.every().day.at("21:30").do(jobToday)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

