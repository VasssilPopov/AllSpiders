import scrapy

class TestItem(scrapy.Item):
    url = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()