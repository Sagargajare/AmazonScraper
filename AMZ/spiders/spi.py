import os

import scrapy
import re
from scrapy.crawler import CrawlerProcess
from ..items import AmzItem

def rater(rating):
    out = re.findall(r"([0-9.]+) out of 5 stars",rating)
    return out[0]




class QuotesSpider(scrapy.Spider):

    name = 'AZ'
    # start_urls = [
    #     'https://www.amazon.in/s?k=men+sunglasses',
    # ]
    myBaseUrl = ''
    start_urls = []


    def __init__(self, category='',pages=1 ,**kwargs):  # The category variable will have the input URL.
        self.myBaseUrl = category
        self.start_urls.append(self.myBaseUrl)
        self.pages = pages
        self.x = 0
        super().__init__(**kwargs)


    custom_settings = {'FEED_URI': 'output.json', 'CLOSESPIDER_TIMEOUT': 60}


    def parse(self, response):
        items = AmzItem()
        #//div/a/span[1]/span[2]/span[2] ---price
        #//div/div[2]/div/span[1]/span/a/i[1] --rating
        #//div/div[2]/div/span[1]/span/a/i[1]/span/text() --rating
        #response.xpath("//div[2]/div[1]/div/div/span/a/div/img/@src").extract() ---img


        for img,name,price,rating in zip(response.xpath("//div[2]/div[1]/div/div/span/a/div/img/@src").extract(),
                                         response.xpath("//div[1]/h2/a/span/text()").extract(),
                                         response.xpath("//div/a/span[1]/span[2]/span[2]/text()").extract(),
                                         response.xpath("//div/div[2]/div/span[1]/span/a/i[1]/span/text()").extract()):
            # print(img+"  "+name+"  "+price+"  "+rater(rating))
            items["img"] =img
            items["name"] = name
            items["price"] = price
            items["Rating"] = rater(rating)

            yield items
        #//div[18]/span/div/div/ul/li[7]/a
        #//div[1]/div[1]/div[1]/div[2]/div/span[3]/div[2]/div[19]/span/div/div/ul/li[7]/a

        # next_page = response.css('li.next a::attr("href")').get()
        if self.x<=self.pages:
            self.x = self.x + 1
            next_page = f"{self.myBaseUrl}&page={self.x}"

            yield response.follow(next_page, self.parse)
# if __name__ == "__main__":
#   process = CrawlerProcess()
#   process.crawl(QuotesSpider,category = "https://www.amazon.in/s?k=men+sunglasses")
#   process.start()