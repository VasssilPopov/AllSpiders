@echo on
scrapy runspider MediapoolSpider.py -o Reports/Mediapool-%1.json -t jsonlines 2> Logs/outputMediapool.txt
@echo on
