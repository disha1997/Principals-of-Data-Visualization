# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ScrapingPipeline:

    def __init__(self):
        self.con = sqlite3.connect('F:/Masters/Principles_of_Data_Visualization/Scrapy_Project/scraping/scraping/amazon_data.db')
        self.cur = self.con.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            name TEXT,
            rating TEXT,
            price TEXT
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute("""
            INSERT INTO products (name, rating, price) VALUES (?, ?, ?)
        """,
        (
            item['name'],
            item['rating'],
            item['price']
        ))
        self.con.commit()
        return item
