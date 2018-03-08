# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NBAItem(scrapy.Item):
    name = scrapy.Field()
    rank = scrapy.Field()
    score = scrapy.Field()
    threeRate = scrapy.Field()
    hitRate = scrapy.Field()
    freeRate = scrapy.Field()


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    platform = scrapy.Field()


class ScheduleItem(scrapy.Item):
    date = scrapy.Field()
    teams = scrapy.Field()
    gameTime = scrapy.Field()
