@echo on
scrapy runspider PIKSpider.py -o Reports/PIK-%1.json -t jsonlines 2> Logs/outputPIK.txt
@echo on
