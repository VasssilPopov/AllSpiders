@echo on
scrapy runspider NewsSpider.py -o Reports/News-%1.json -t jsonlines 2> Logs/outputNews.txt
@echo on
