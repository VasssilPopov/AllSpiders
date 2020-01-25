#Today = date.today().strftime("%Y-%m-%d")
#print Today

import jsonlines
import os
import system
from datetime import date, timedelta
import sys
print 'start'


'Get the dates in the YYYY-mm-dd format'
Today = date.today().strftime("%Y-%m-%d")
Today = '2020-01-22'


system('Python SummaryReport.py>_DailySummaryReports/'+Today+'.txt')