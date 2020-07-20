# 导入第三方库
# requests用来获取网页
import requests
# lxml.etree以解析xml的方式来解析html格式文件
from lxml import etree

# 要爬取的html所在网址
url = "https://maoyan.com/films?showType=2"

# 模仿浏览器的报头
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
connection = 'keep-alive'
# 使用一个字典之前一定要先声明
header =  {}
header['user-agent'] = user_agent
header['accept'] = accept
header['connection'] = connection

response = requests.get(url, headers = header)
# print(response.text)
print(f'返回码：{response.status_code}')

# 把html当作xml来处理
selector = etree.HTML(response.text)

# 这里直接取selector对象返回的列表当中我们需要的元素
# 用strip函数去除字符串两端的无效字符
mylist = []
for i in range(3, 11):
    # 电影名称
    print("i =", i)
                               # //*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[1]/span
    film_name = selector.xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd[{i}]/div[1]/div[2]/a/div/div[1]/span/text()')
    # 字符串当中有双引号，该字符串就应该用单引号，反之亦然
    print(f'电影名称：{film_name}')
    print(type(film_name))

    # 电影类型
    film_class = selector.xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd[{i}]/div[1]/div[2]/a/div/div[2]/text()')[1].strip()
    print(f'电影类型：{film_class}')

    # 上映时间
    film_releaseTime = selector.xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd[{i}]/div[1]/div[2]/a/div/div[4]/text()')[1].strip()
    print(f'上映时间：{film_releaseTime}')

    mylist.append([film_name, film_class, film_releaseTime])

print(mylist)
# 把爬取的内容保存为csv格式文件
import pandas as pd
movie = pd.DataFrame(data = mylist)
# windows的excel打开utf-8格式l乱码。需要更换编码格式，所以最好保存为gbk格式
movie.to_csv('./movie1.csv', encoding = 'utf-8', index = False, header = False)