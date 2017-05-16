echo off
scrapy runspider PIKSpider.py -o Reports/PIK-%1.json -t jsonlines 2> Log/output.txt
echo on