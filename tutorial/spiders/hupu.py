# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import NBAItem
from tutorial.items import NewsItem
from tutorial.items import ScheduleItem

# 球员数据
class NBASpider(scrapy.Spider):
    name = "nba"
    allowed_domains = ["nba.hupu.com"]
    start_urls = ['https://nba.hupu.com/stats/players']

    def parse(self, response):
        players = response.css('.players_table tr')
        for (index, player) in enumerate(players):

            if index == 0:
                continue
            else:
                item = NBAItem()
                item['name'] = player.xpath('td[2]/a/text()').extract_first()
                item['rank'] = player.xpath('td[1]/text()').extract_first()
                item['score'] = player.xpath('td[4]/text()').extract_first()
                item['threeRate'] = player.xpath('td[8]/text()').extract_first()
                item['hitRate'] = player.xpath('td[6]/text()').extract_first()
                item['freeRate'] = player.xpath('td[10]/text()').extract_first()
                yield item
        next = response.css('.pages_box .page_num + a::attr("href")').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)


# 虎扑新闻
class NBASpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["hupu.com"]
    start_urls = ['https://voice.hupu.com/nba']

    def parse(self, response):
        news = response.css('.news-list>ul>li')
        for (index, new) in enumerate(news):
            item = NewsItem()
            if new.xpath('div[1]/h4/a/text()').extract_first():
                item['title'] = new.xpath('div[1]/h4/a/text()').extract_first()
                item['time'] = new.xpath('div[2]/span[1]/a/text()').extract_first()
                item['platform'] = new.xpath('div[2]/span[1]/span/a/text()').extract_first()
                yield item
        next = response.css('.voice-paging a:last-child::attr("href")').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)


# 比赛日期
class ScheduleSpider(scrapy.Spider):
    name = "schedule"
    allowed_domains = ["hupu.com"]
    start_urls = ['https://nba.hupu.com/schedule']

    def parse(self, response):
        schedules = response.css('.players_table tbody tr.left')
        for (index, schedule) in enumerate(schedules):
            item = ScheduleItem()
            if 'linglei' in schedule.xpath('./@class').extract_first():
                tempDate = schedule.xpath('td/text()').extract_first()
            else:
                item['date'] = tempDate
                item['teams'] = schedule.xpath('td[2]/a[1]/text()').extract_first() + 'vs' +schedule.xpath('td[2]/a[2]/text()').extract_first()
                item['gameTime'] = schedule.xpath('td[1]/text()').extract_first()
                yield item
        next = response.css('.choosedare .a b:nth-of-type(2) a::attr("href")').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
