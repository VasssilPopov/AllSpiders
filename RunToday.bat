@echo on
scrapy runspider Blitz/BlitzSpider.py -o Blitz/Reports/Blitz-%1.json -t jsonlines 2> Blitz/Logs/outputBlitz.txt
scrapy runspider Mediapool/MediapoolSpider.py -o Mediapool/Reports/Mediapool-%1.json -t jsonlines 2> Mediapool/Logs/outputMediapool.txt
@echo on
