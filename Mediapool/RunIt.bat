@echo off
scrapy runspider MediapoolSpider.py -o Reports/Mediapool-%1.json -t json 2> Logs/output.txt
@echo on
