#!Python3
"""
Spiderman web crawler

Run:
scrapy crawl craig -o file.csv -t csv

"""
from scrapy.spiders import Spider
from scrapy.selector import Selector
from spiderman.items import SpidermanItem
from scrapy.http import Request

class pmSpider(Spider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["https://seattle.craigslist.org/search/eng"]

    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.xpath("//p[@class='result-info']")
        items = []
        for titles in titles:
            item = SpidermanItem()
            item["title"] = titles.xpath("a/text()").extract()
            item["link"] = titles.xpath("a/@href").extract()
            items.append(item)
        return items