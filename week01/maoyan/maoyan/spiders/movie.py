import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector
from lxml import etree

class MovieSpider(scrapy.Spider):
    def __init__(self):
        print(' Init MovieSpider')
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=2']

    def parse(self, response):
        # print(response.text)
        print('Running parse')
        item = MaoyanItem()
        with open('maoyan.html', 'w') as html:
            html.write(response.text.replace("<dd>", "</dd><dd>"))
        # selector = Selector(response = response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl')
        # selector = Selector(response = response)
        selector = etree.HTML(response.text.replace("<dd>", "</dd><dd>"))
        for i in range(1, 11):
            print('Running movie.py')
            # 电影名称
                                       # //*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[1]/span
            item['name'] = selector.xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd[{i}]/div[1]/div[2]/a/div/div[1]/span/text()')[0]
            # 电影类型
            item['type'] = selector.xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd[{i}]/div[1]/div[2]/a/div/div[2]/text()')[1].strip()
            # 上映时间
            item['release'] = selector.xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd[{i}]/div[1]/div[2]/a/div/div[4]/text()')[1].strip()
            yield item 