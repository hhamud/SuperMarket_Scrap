# -*- coding: utf-8 -*-
import mysql.connector





class Default_Values(object):
    """
    a pipeline that sets the default value of 0 for each field if scrapy does not find any information on the website
    
    """

    def process_item(self, item, spider):
        item.setdefault('Energy', '0')
        item.setdefault('Carbohydrate', '0')
        item.setdefault('Sugars', '0')
        item.setdefault('Fat', '0')
        item.setdefault('Saturates','0')
        item.setdefault('Protein', '0')
        item.setdefault('Fibre', '0')
        item.setdefault('Salt', '0')



        return item








class ShopScrapdb(object):

    def __init__(self):
        """
        
        Initializes database connection.
        
        
        """
        self.conn = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='shopscrapdb'
        )

        self.cursor = self.conn.cursor()


    def process_item(self, item, spider):

        """
        process pipeline that stores the items scraped into the MYSQL database
        
        
        """


        sql_stock = """INSERT INTO stock(
            name, energy, carbohydrates, sugars, fats, saturates, protein, fibre, salt)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        
        sql_price = """INSERT INTO prices(price, date)
            VALUES (%s, %s)"""
           
        sql_supermarket = """INSERT INTO supermarkets(name, stock_url)
            VALUES (%s, %s)"""


    
        stock_data = [
            item["Name"],
            item["Energy"],
            item["Carbohydrate"],
            item["Sugars"],
            item["Fat"],
            item["Saturates"],
            item["Protein"],
            item["Fibre"],
            item["Salt"] 
        ]



        price_data = (
            item["Price"],
            item["Date"]
        )

        supermarket_data = (
            item["Supermarket"],
            item["item_url"]
        )

        try:
            self.cursor.execute(sql_stock, stock_data)
            self.cursor.execute(sql_price, price_data)
            self.cursor.execute(sql_supermarket, supermarket_data)
            self.conn.commit()
        except:
            self.conn.rollback()
            
        
        
        return item

        

    def close_spider(self, item, spider):
        self.cursor.close()
        self.conn.close()

     