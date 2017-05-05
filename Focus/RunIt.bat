@echo off
scrapy runspider FocusSpider.py -o Reports/Focus-%1.json -t json 2> Logs/output.txt
@echo on
