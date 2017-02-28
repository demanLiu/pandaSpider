# -*- coding: utf-8 -*-
import scrapy


class AnchorSpider(scrapy.Spider):
    name = "anchor"
    allowed_domains = ["www.panda.tv"]
    start_urls = ['http://www.panda.tv/all']

    def parse(self, response):
        sel = scrapy.Selector(response)
        lis = response.selector.xpath('//ul[@id="later-play-list"]/li').extract()
        for content in lis: 
            print(content)
            break;
