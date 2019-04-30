import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic_crawler"
    def start_requests(self):
        pass

    def parse(self, response):
        pass