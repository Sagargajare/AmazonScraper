import os

import scrapy
import re
from scrapy.crawler import CrawlerProcess
from AMZ.spiders.spi import QuotesSpider

if os.path.exists("output.json.json"):
  os.remove("output.json.json")
if __name__ == "__main__":

  url = input("Enter Url Of Amazon Example <https://www.amazon.in/s?k=sun+glasses> : -")
  pages = int(input("No. of pages"))
  print("After Process the output willbe in output.json")
  process = CrawlerProcess()

  process.crawl(QuotesSpider,category = url,pages = pages)
  process.start()