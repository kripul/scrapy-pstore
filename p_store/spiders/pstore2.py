import scrapy


class Pstore2Spider(scrapy.Spider):
    name = 'pstore2'
    allowed_domains = ['p-store.com']
    start_urls = ['http://p-store.com/']

    def parse(self, response):
        pass
