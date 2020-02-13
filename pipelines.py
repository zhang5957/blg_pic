# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
class BmwLianxiPipeline(object):
    def __init__(self):
        # os.path.dirname(__file__)是获得pipelines的目录，os.path.dirname(os.path.dirname(__file__)是获得pipelines的上一级目录。os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')是images的位置
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
    def process_item(self, item, spider):
        title = item['title']
        urls = item['urls']
        title_path = os.path.join(self.path, title)
        if not os.path.exists(title_path):
            os.mkdir(title_path)

        for url in urls:
            image_name = url.split('_')[-1]
            request.urlretrieve(url, os.path.join(title_path, image_name))

        return item
