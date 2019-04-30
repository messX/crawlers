class TripAdvHelper:
    @staticmethod
    def extract(response):
        '''function to extract response'''
        name = response.xpath('//h1[@id="HEADING"]/text()').extract()
        return dict(name=name)