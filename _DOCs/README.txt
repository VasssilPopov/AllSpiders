About data (Updated at 2017-06-14)

The main folder is AllSpiders.

It contains the following subfolders:
        _DailySummaryReports - reports about records collected by data sources
	_DOCs 		- documents related to the system
	_LIBRARY	- common modules related to all spiders
	RunAllSpiders.bat - It run all spiders 
			    !!! Current date must be entered as a parameter 
				Date format must be: YYYY-mm-dd  (2017-05-06)
				It will serve to be include into report's name
				for eachone running spider (Blitz-2017-05-01.json)

	Blitz			- information about specific spider. The same set will be 				  repeated for each spider

		BlitzSpider.py	- spider program
		Cleaning.py	- specific to Blitz data verification program
		RunIt.bat 	- It run only current spider (BlitzSpider at the moment)
			    	!!! Current date must be entered as a parameter 
				Date format must be: YYYY-mm-dd  (2017-05-06)
				It will serve to be include into report's name
				for the current running spider (Blitz-2017-05-01.json)

		Logs 		- subdirectory. 
	  	    outputBlitz.txt 	- contains printout of latest BlitzSpider run .
				  
		Reports		- subdirectory.
		    Blitz-2017-05-01.json  - spider result
		    Blitz-2017-05-02.json  - spider result
		    Blitz-2017-05-03.json  - spider result
		    Blitz-2017-05-04.json  - spider result

	- Each spider will have his own directory
	- Inside spider's directory will be located spider's specific data and tools 		  	  (Cleaning.py)
	- Report's file name are formed as follow: <Spider name>-YYYY-MM-DD.json
	  (Blitz-2017-05-01.json). This way the names can be easily ordered.
	- Outside spider's directory will be located all common tools.
          So runing RunAllSpiders.bat we should expect batch to run consecutively 
	  each spider and applay the date parameter 
	
Usage 	Run daily procedure

	We can start daily procedure using console by two ways:
	-Change directory cd _AllSpiders
	- RunAllSpiders - it will run '_DailySummaryReports'
	  or directly writing _DailySummaryReports
	as result we will see similar output
------------------------------------------------------------------------------------------------
C:\STUDY_SPIDERS\_AllSpiders>runallspiders

C:\STUDY_SPIDERS\_AllSpiders>Python RunAllSpiders.py
Script Version:  0.1
Today: 2017-06-14 --------------------
---------- Blitz v(1.0) ----------
url: https://www.blitz.bg/politika selected: 15
url: https://www.blitz.bg/politika?page=2 selected: 15
url: https://www.blitz.bg/politika?page=3 selected: 15
url: https://www.blitz.bg/politika?page=4 selected: 15
---------- Mediapool v(1.0) ----------
url: http://www.mediapool.bg/today.html selected: 58
Yesterday: 2017-06-13 --------------------
---------- Dnevnik v(1.0) ----------
url: http://www.dnevnik.bg/allnews/2017/06/13/ selected: 104
---------- Focus v(1.0) ----------
url: http://www.focus-news.net/news/Yesterday/ selected: 360
---------- News v(1.0) ----------
url: https://news.bg/yesterday selected: 21
url: https://news.bg/yesterday?page=2 selected: 21
url: https://news.bg/yesterday?page=3 selected: 21
url: https://news.bg/yesterday?page=4 selected: 21
url: https://news.bg/yesterday?page=5 selected: 2
---------- OffNews v(1.0) ----------
url: https://m.offnews.bg/2017-06-13/ selected: 20
url: https://m.offnews.bg/2017-06-13/?page_which=20 selected: 20
url: https://m.offnews.bg/2017-06-13/?page_which=40 selected: 20
url: https://m.offnews.bg/2017-06-13/?page_which=60 selected: 20
url: https://m.offnews.bg/2017-06-13/?page_which=80 selected: 6
---------- PIK v(1.0) ----------
url: http://pik.bg/novini-za-13-06-2017.html selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=2 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=3 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=4 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=5 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=6 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=7 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=8 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=9 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=10 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=11 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=12 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=13 selected: 30
url: http://pik.bg/novini-za-13-06-2017.html?page=14 selected: 14

------------------------------------------------------------------------------------------------






How to get sources 
	1. Create a directory where all stuff will stay.
		md Insects
	2. Go in
		cd Insects
	3. Create the local repository
		git init
	4. Get all sources into c:/Insects
		git clone https://github.com/VasssilPopov/AllSpiders.git

	
