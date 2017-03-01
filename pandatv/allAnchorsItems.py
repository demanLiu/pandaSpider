# -*- coding: utf-8 -*-
#    熊猫tv所有直播页列表item

import scrapy


class AnchorsItems(scrapy.Item):
     anchorUrl = scrapy.Field()
     videoTitle = scrapy.Field()
     videoNickName = scrapy.Field()
     videoNumber = scrapy.Field()
     videoCategory = scrapy.Field()
