import scrapy
from crawlers.items import CrawlersItem


class TripAdvItem(CrawlersItem):
    # define the fields for your item here like:
    name = scrapy.Field()
