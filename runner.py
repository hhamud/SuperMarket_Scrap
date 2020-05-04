import scrapy
import scrapy_splash
from scrapy.crawler import CrawlerProcess
from shopscrap.spiders.shop_scrap import ShopScrap

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'data.json'
})

process.crawl(ShopScrap)
process.start()