from crawlers.pipelines import CrawlersPipeline


class TripAdvPipeline(CrawlersPipeline):
    def process_item(self, item, spider):
        '''store items somewhere'''
        print("store", item)
        return item
