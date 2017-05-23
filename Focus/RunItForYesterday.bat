@echo off
scrapy runspider FocusSpider.py -o Reports/Focus-%1.json -t jsonlines 2> Logs/output.txt
python cleaning.py
@echo on
