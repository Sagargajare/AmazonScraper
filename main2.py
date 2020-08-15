import os

import scrapy
import re
from scrapy.crawler import CrawlerProcess
from AMZ.spiders.spi import QuotesSpider

if os.path.exists("c.json"):
  os.remove("c.json")
if __name__ == "__main__":
  process = CrawlerProcess()
  process.crawl(QuotesSpider,category = "https://www.amazon.in/s?k=sun+glasses")
  process.start()