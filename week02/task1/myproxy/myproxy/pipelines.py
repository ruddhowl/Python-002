# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from myproxy.spiders.maoyan import MaoyanSpider as m
class MyproxyPipeline:
    def __init__(self):
        print('Init MyproxyPipeline')
    def process_item(self, item, spider):
        name = item['name']
        tp = item['tp']
        release = item['release']
        sql = f"insert into movie values ('{name}','{tp}','{release}')"

        try:
            cur = m.conn.cursor()
            cur.execute(sql)
            cur.close
            m.conn.commit()
        except Exception as e:
            print("Error happened!!!!!!!!!!!!!!!!!!")
            print(e)
            m.conn.rollback()
            
        print('Running pipelines.py')
        return item
