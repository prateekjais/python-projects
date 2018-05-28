# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class GiveindiaPipeline(object):
    def process_item(self, item, spider):
        conn = psycopg2.connect(hostname = "localhost", database = "public", user = "postgres", password = "pgadmin")
        cur = conn.cursor()
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            cur.execute("insert", ('a','b','c','d','e'))
            log.msg("List added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item
