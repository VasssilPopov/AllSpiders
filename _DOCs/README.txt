About data

The main folder is Spiders.

It contains the following subfolders:
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
	  	    output.txt 	- contains printout of latest BlitzSpider run .
				  
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
	  each spider and applay the same date parameter 
	

How to get sources 
	1. Create a directory where all stuff will stay.
		md Insects
	2. Go in
		cd Insects
	3. Create the local repository
		git init
	4. Get all sources into c:/Insects
		git clone username@host:/path/to/repository


