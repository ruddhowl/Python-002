import scrapy
from myproxy.items import MyproxyItem
from scrapy.selector import Selector
from lxml import etree
import pymysql
from myproxy.settings import dbInfo

class MaoyanSpider(scrapy.Spider):
    def __init__(self):
        print(' Init MovieSpider')
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']
    conn = pymysql.connect(
        host=dbInfo['host'],
        port=dbInfo['port'],
        user=dbInfo['user'],
        password=dbInfo['password'],
        db=dbInfo['db']
    )

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        print('Running parse')
        item = MyproxyItem()
        with open('maoyan.html', 'w') as html:
            html.write(response.text.replace("<dd>", "</dd><dd>"))

        try:
            elem = Selector(response = response).xpath('//div[@class="movie-hover-info"]')
            print(elem.extract_first())
            print(type(elem.extract()))
            # 这里直接取selector对象返回的列表当中我们需要的元素
            # 用strip函数去除字符串两端的无效字符
            cnt = 0
            for selector in elem:
                if 10 == cnt:
                    break
                cnt += 1
                print('Running movie.py')
                # 电影名称
                                           # //*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[1]/span
                item['name'] = selector.xpath(f'./div[1]/span/text()')[0].extract()
                # 电影类型
                item['type'] = selector.xpath(f'./div[2]/text()')[1].extract().strip()
                # 上映时间
                item['release'] = selector.xpath(f'./div[4]/text()')[1].extract().strip()
                yield item 
        except Exception as e:
            print("Error happened!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(e.__traceback__)
        finally:
            self.conn.close()
        
