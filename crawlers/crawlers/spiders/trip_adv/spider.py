import scrapy
from crawlers.spiders.base_spider import BasicSpider
from crawlers.spiders.trip_adv.constants import CrawlerConstantsTripAdv
from crawlers.spiders.trip_adv.helpers import TripAdvHelper


class TripAdvSpider(BasicSpider):
    name = "tripadv_crawler"
    def start_requests(self):
        '''define start urls logic here'''
        urls = [
            'https://www.tripadvisor.in/Attractions-g187147-Activities-c63-zfq196559,187185,187123,8791126,1462420,196646,676160,616096,1055336,10401392,187182,227610,4039848,1075717,660739,482937,196661,4201013,1826218,1061563,2436295,196576,187165,644122,660952,608778,187201,644104.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        '''define parse logic here'''
        url = response.url
        meta = response.meta
        result = TripAdvHelper.extract(response)
        yield result
