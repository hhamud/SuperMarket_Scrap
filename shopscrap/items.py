# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopscrapItem(scrapy.Item):
    Name = scrapy.Field()
    Price = scrapy.Field()
    item_url = scrapy.Field()
    Energy = scrapy.Field()
    Fat = scrapy.Field()
    Carbohydrate = scrapy.Field()
    Saturates = scrapy.Field()
    Sugars = scrapy.Field()
    Fibre = scrapy.Field()
    Protein = scrapy.Field()
    Salt = scrapy.Field()
    Date = scrapy.Field()
    Supermarket = scrapy.Field()