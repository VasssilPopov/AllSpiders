from scrapy.exceptions import DropItem
from datetime import date, timedelta

class FilterOnlyYesterdayPipeline(object):
    
    yesterday = date.today() - timedelta(1)
    Yesterday = yesterday.strftime("%Y.%m.%d")
    
    
    def process_item(self, item, spider):
        if item['date'] == Yesterday:
            return item
        else:
            raise DropItem("Out of scope %s" % item)