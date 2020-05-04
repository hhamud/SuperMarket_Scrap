# -*- coding: utf-8 -*-





#?: each pipeline class can be given a different priority in the settings, (lower = greater priority)

from __future__ import absolute_import
from sqlalchemy.orm import sessionmaker
import pymysql
from shopscrap.Database import Prices, Supermarkets, Stock, connect_db
from scrapy.exceptions import DropItem






class ShopScrapdb(object):

    def __init__(self):
        """
        
        Initializes database connection and sessionmaker.
        Creates deals table.
        
        """
        engine = connect_db()
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):

        """
        process pipeline

        first checks if it already exists in the database,
        then stores the items into the MYSQL database
        
        
        """
        session = self.Session()
        prices = Prices()
        supermarket = Supermarkets()
        stock = Stock()

        x = item['Name']

        name_match = session.query(Stock).get(f'{x}')

        if item['Name'] != name_match:
            stock.name = item['Name'] 
            prices.price = item['Price']
            supermarket.stock_url = item['item_url']
            prices.date = item['Date'] 
            supermarket.name = item['Supermarket'] 
            if item['Saturates']:
                stock.saturates = item['Saturates']
            elif item['Sugars']:
                stock.sugars = item['Sugars']
            elif item['Energy']:
                stock.energy = item['Energy']
            elif item['Fat']:
                stock.fats =  item['Fat'] 
            elif item['Carbohydrate']:
                stock.carbohydates =  item['Carbohydrate']
            elif item['Fibre']:
                stock.fibre = item['Fibre'] 
            elif item['Protein']:
                stock.protein = item['Protein']
            elif item['Salt']:
                stock.salt = item['Salt'] 
        else:
            prices.price = item['Price']
            prices.date = item['Date'] 
            supermarket.name = item['Supermarket']       
        try:
            session.add(stock)
            session.add(prices)
            session.add(supermarket)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()


        return item
