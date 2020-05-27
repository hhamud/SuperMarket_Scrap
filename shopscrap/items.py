# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopscrapItem(scrapy.Item):
    name = scrapy.Field()
    nutrition = scrapy.Field()
    price = scrapy.Field()
    date = scrapy.Field()