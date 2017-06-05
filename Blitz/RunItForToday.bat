@echo on
scrapy runspider BlitzSpider.py -o Reports/Blitz-%1.json -t jsonlines 2> Logs/outputBlitz.txt
@echo on
