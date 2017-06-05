@echo on
scrapy runspider Dnevnik/DnevnikSpider.py -o Dnevnik/Reports/Dnevnik-%1.json -t jsonlines 2> Dnevnik/Logs/outputDnevnik.txt
scrapy runspider News/NewsSpider.py -o News/Reports/News-%1.json -t jsonlines 2> News/Logs/outputNews.txt
scrapy runspider OffNews/OffNewsSpider.py -o OffNews/Reports/OffNews-%1.json -t jsonlines 2> OffNews/Logs/outputOffNews.txt
scrapy runspider PIK/PIKSpider.py -o PIK/Reports/PIK-%1.json -t jsonlines 2> PIK/Logs/outputPIK.txt
scrapy runspider Focus/FocusSpider.py -o Focus/Reports/Focus-%1.json -t jsonlines 2> Focus/Logs/outputFocus.txt
@echo on
