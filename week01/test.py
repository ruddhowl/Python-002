# 导入第三方库
# lxml.etree以解析xml的方式来解析html格式文件
from lxml import etree
htm = ''
with open('maoyan.html') as html:
    htm = html.read()
# 把html当作xml来处理
htm.replace("<dd>", "</dd><dd>")
selector = etree.HTML(htm)

# 这里直接取selector对象返回的列表当中我们需要的元素
# 用strip函数去除字符串两端的无效字符
mylist = []
for i in range(1, 11):
    # 电影名称
    print("i =", i)
                               # //*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[1]/span
    film_name = selector.xpath(f'//*[@id="app"]/div/div[2]/div[2]/dl/dd[{i}]/div[1]/div[2]/a/div/div[1]/span/text()')[0]
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