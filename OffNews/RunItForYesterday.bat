@echo on
scrapy runspider OffNewsSpider.py -o Reports/OffNews-%1.json -t jsonlines 2> Logs/outputOffNews.txt
@echo on
