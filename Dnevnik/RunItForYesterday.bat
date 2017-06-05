@echo on
scrapy runspider DnevnikSpider.py -o Reports/Dnevnik-%1.json -t jsonlines 2> Logs/outputDnevnik.txt
@echo on
