
import scrapy
import re 
import logging
from scrapy.exceptions import ScrapyDeprecationWarning
from shopscrap.items import ShopscrapItem
from scrapy.http import HtmlResponse, Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashRequest, SplashResponse
from datetime import datetime
import random
import requests


logging.basicConfig(filename='error.log',level=logging.WARNING)
logging.warning('Spider warnings')


class ShopScrap(CrawlSpider):
    name = 'ShopScrap'
    start_urls = ['http://groceries.asda.com/product/cornflakes-honey-nut/kelloggs-crunchy-nut-corn-flakes/19140/']
    allowed_domains = ['groceries.asda.com']
  
        
    def start_requests(self):
        with open('proxy/proxy-list.txt', 'r') as f:
            listcomp = [i for i in f]
            x = random.choice(listcomp).strip('\n')
            try:
                base = 'http://'
                self.ports = x.split(":")[1]
                self.ip = x.split(":")[0]
                self.proxy = base + self.ip
                proxies = {f'{base}' :f'{self.proxy}:{self.ports}'}
                print(proxies)
                print(self.ip)
                requests.get(url="http://google.co.uk",
                    proxies=proxies
                )
            except IOError:
                print('Connection error!, proxy %s failed' % (x))
            else:
                print('success!, proxy %s worked' % (x))

                self.proxy_link = """function main(splash)
                    splash:on_request(function(request)
                        request:set_proxy{{
                            host = "{ip}",
                            port = {port},
                            type = "HTTP"
                        }}
                        end)
                    assert(splash:wait(10))
                    return splash:html()
                    end""".format(
                        ip=self.ip,
                        port=self.ports
                    )
            
                

                for url in self.start_urls:
                    yield SplashRequest(url=url,callback=self.parse_item, dont_filter=False ,args={
                        'url': url, 
                        'wait': 10, 
                        'timeout': 30, 
                        'lua_source': self.proxy_link,
                        'proxy': '{proxy}:{port}'.format(proxy=self.proxy,port=self.ports)
                        
                        })
                # 
                #'js_source': 'document.body'
                #endpoint='render.html'
    
    def parse_item(self, response):
        item = ShopscrapItem()

        table1 = response.css('div.pdp-description-reviews__nutrition-cell.pdp-description-reviews__nutrition-cell--grouped::text').getall()
        table2 = response.css('div.pdp-description-reviews__nutrition-cell.pdp-description-reviews__nutrition-cell--details::text').getall()
    

               
        Name = response.css('h1.pdp-main-details__title::text').get()
        item_url = response.url
        Price = response.css('strong.co-product__price.pdp-main-details__price::text').get()

        Date = datetime.today()
        Supermarket = 'Asda'
        item['Price'] = Price
        item['Name'] = Name
        item['item_url'] = item_url
        item['Date'] = Date
        item['Supermarket'] = Supermarket

    
        for i,j in enumerate(table1):
            if 'of which saturates' in j:
                Saturates = table1[i+1]
                item['Saturates'] = Saturates 
            elif 'of which sugars' in j:
                Sugars = table1[i+1]
                item['Sugars'] = Sugars


        for i,j in enumerate(table2):
            if "Energy" in j:
                Energy = table2[i+1]
                item['Energy'] = Energy
            elif "Fat" in j:
                Fat = table2[i+1]
                item['Fat'] = Fat
            elif "Carbohydrate" in j:
                Carbohydrate = table2[i+1]
                item['Carbohydrate'] = Carbohydrate
            elif "Fibre" in j:
                Fibre = table2[i+1]
                item['Fibre'] = Fibre
            elif "Protein" in j:
                Protein = table2[i+1]
                item['Protein'] = Protein
            elif "Salt" in j:
                Salt = table2[i+1]
                item['Salt'] = Salt        
        
        yield item



        for next in response.css('.co-product__anchor::attr(href)').getall():
            link = next.split("?")[0]
            yield SplashRequest(response.urljoin(link), 
                dont_filter=False, 
                callback=self.parse_item,
                args={'wait':10.0,
                    'timeout': 30, 
                    'lua_source': self.proxy_link,
                    'js_source': 'document.body', 
                    'proxy': '{proxys}:{port}'.format(proxys=self.proxy,
                    port=self.ports)})


                
                            # self.proxy_link = """splash:on_request(function(request)
                #                         request:set_proxy{{
                #                             host = {proxys},
                #                             port = {port}, 
                #                             type = 'HTTP'}}
                #                         return splash:html()
                #                     end)""".format(
                #     proxys=self.proxy,
                #     port=self.ports)
                # assert(splash:go(args.url))
                #'js_source': 'document.body',
                #assert(splash:wait(10))