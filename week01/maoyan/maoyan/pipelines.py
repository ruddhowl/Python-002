# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd


class MaoyanPipeline:
    def __init__(self):
        print('Init MaoyanPipeline')
    def process_item(self, item, spider):
        name = item['name']
        type = item['type']
        release = item['release']
        list = [[name, type, release]]
        # 把爬取的内容保存为csv格式文件
        movie = pd.DataFrame(data = list)
        movie.to_csv('./movie2.csv', encoding = 'utf-8', index = False, header = False, mode = 'a')
        print('Running pipelines.py')
        return item
