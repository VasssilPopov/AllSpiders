# -*- coding: utf-8 -*-

from os import system

import schedule
import time

def jobYesterday():
    system('Python RunYesterdaySpiders.py ')
    print("I'm working... "+str(time.ctime()))

def jobToday():
    system('Python RunTodaySpiders.py ')
    print("I'm working... "+str(time.ctime()))

#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at("00:15").do(jobYesterday)
schedule.every().day.at("23:15").do(jobToday)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

