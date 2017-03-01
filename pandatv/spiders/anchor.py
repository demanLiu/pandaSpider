# -*- coding: utf-8 -*-
import scrapy
from pandatv.allAnchorsItems import AnchorsItems

class AnchorSpider(scrapy.Spider):
    name = "anchor"
    allowed_domains = ["www.panda.tv"]
    start_urls = ['http://www.panda.tv/all']

    def parse(self, response):
        prefix = 'http://www.panda.tv'
        item = AnchorsItems()
        lis = response.selector.xpath('//ul[@id="later-play-list"]/li')
        for content in lis: 
            item['anchorUrl'] = prefix+ content.xpath('.//a/@href').extract()[0]
            item['videoTitle'] = content.xpath('.//div[@class="video-title"]/@title').extract()[0]
            item['videoNickName'] = content.xpath('.//div[@class="video-info"]/span[@class="video-nickname"]/text()').extract()[0]
            item['videoNumber'] = content.xpath('.//div[@class="video-info"]/span[@class="video-number"]/text()').extract()[0]
            item['videoCategory'] = content.xpath('.//div[@class="video-info"]/span[@class="video-cate"]/text()').extract()[0]
            yield item
