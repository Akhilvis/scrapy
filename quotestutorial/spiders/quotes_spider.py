import scrapy
from ..items import QuotestutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        # quote = response.css(".author::text").extract()
        # yield {"quote": quote}

        items = QuotestutorialItem()

        for quote in response.css('div.quote'):
            qte = quote.css('.text::text').extract()[0]
            author = quote.css('.author::text').extract()[0]
            tags = quote.css('a.tag::text').extract()

            items['quote'] = qte
            items['author'] = author
            items['tags'] = tags

            yield items
