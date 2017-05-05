@echo on
scrapy runspider BlitzSpider.py -o Reports/Blitz-%1.json -t json 2> Logs/output.txt
@echo on
