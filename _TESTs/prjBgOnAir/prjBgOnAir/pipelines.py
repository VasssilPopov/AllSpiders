# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class PrjbgonairPipeline(object):
    # def process_item(self, item, spider):
        # return item
from scrapy.exceptions import DropItem
from datetime import date, timedelta

class FilterOnlyYesterdayPipeline(object):
    
    yesterday = date.today() - timedelta(1)
    Yesterday = yesterday.strftime("%Y.%m.%d")
    
    
    def process_item(self, item, spider):
        if item['date'] == self.Yesterday:
            return item
        else:
            raise DropItem("Out of scope %s" % item)