
import scrapy
import logging
from scrapy.exceptions import ScrapyDeprecationWarning
from shopscrap.items import ShopscrapItem
from scrapy.http import Request, FormRequest
from scrapy.spiders import CrawlSpider
from datetime import datetime
import requests
import xml.etree.ElementTree as ET 
import json



logging.basicConfig(filename='error.log',level=logging.WARNING)
logging.warning('Spider warnings')


class ShopScrap(CrawlSpider):
    name = 'ShopScrap'
    start_urls = ['https://groceries.asda.com/api/items/catalog']
  
    #     start_urls = [
    #     'https://groceries.asda.com/product/cornflakes-honey-nut/kelloggs-corn-flakes-big-pack/910000043501',
    #     'https://groceries.asda.com/product/coke-cola/coca-cola-zero-sugar-cans/80996825',
    # ]
    allowed_domains = ['https://groceries.asda.com/api/items/catalog']

    # def request_site_index(self):
    #     url_list = 'https://groceries.asda.com/sitemap-products.xml'
    #     site_index = requests.get(url_list)
    #     with open('site_index_links.xml', 'wb') as f:
    #         f.write(site_index.content)

    # def parse_xml(self):
    #     parse_file = ET.parse('site_index_links.xml')
    #     file_root = parse_file.getroot()
    #     prod_id_list = [] 
    #     for i in file_root.findall('url'):
    #         prod_link = i.find('loc').text 
    #         prod_id = prod_link.split("/")[-1] 
    #         prod_id_list.append(prod_id)
        
    #     return prod_id_list



    def start_requests(self):
        url_list = 'https://groceries.asda.com/sitemap-products.xml'
        site_index = requests.get(url_list)
        with open('site_index_links.xml', 'wb') as f:
            f.write(site_index.content)
        parse_file = ET.parse('site_index_links.xml')
        file_root = parse_file.getroot()
        print(file_root)
        prod_id_list = [] 
        for i in file_root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            prod_link = i.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text 
            prod_id = prod_link.split("/")[-1] 
            prod_id_list.append(prod_id)

        for url in self.start_urls:
            for x in prod_id_list:
                body = {"consumer_contract": "webapp_pdp",
                        "item_ids": [f"{x}"],
                        "0": f"{x}",
                        "request_origin": "gi",
                        "store_id": "4565"}
                header = {'Content-Type': 'application/json'}
                print(body)
                yield scrapy.Request(url=url, method='POST', body=json.dumps(body), callback=self.parse_item, headers=header)

    
    def parse_item(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        item = ShopscrapItem()
        jsonresponse = json.loads(response.text)
        print(jsonresponse)

        item['data_input'] = jsonresponse

        yield item
        # for url in self.start_urls:
        #     for x in prod_id_list:
        #         body = {"item_ids": [f"{x}"],
        #                         "0": f"{x}",
        #                         "request_origin": "gi",
        #                         "store_id": "4565"}
                        
        #         yield scrapy.Request(url=url, method='POST',formdata=body ,callback=self.parse_item)





                
