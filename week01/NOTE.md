# 学习笔记

## python爬虫相关的库

requests：获取网页（python自带的urllib库步骤较为繁琐，所以通常使用第三方requests库来获取网页资源）

BeautifulSoup：解析网页内容

lxml.etree：把html格式当作xml来解析，用xpath来匹配网页中的元素

## python爬虫框架scrapy

所谓框架，就是一个半成品，辅助你完成开发的利器。

##### scrapy数据流：

https://docs.scrapy.org/en/latest/topics/architecture.html

##### scrapy开发的一般流程：

创建项目、创建爬虫、爬取网页、提取数据（创建实体、提取数据）、数据存储

##### scrapy常用的交互式命令：

scrapy startproject project_name # 创建项目

scrapy genspider example example.com # 创建爬虫

对应爬虫类：

```python
class ExampleSpider(scrapy.Spider):
	name = "example"
	allowed_domains = {"example.com"}
	start_urls = {"https://www.example.com/"}
```

scrapy crawl example # 启动爬虫

scrapy shell https://www.example.com # 打开scrapy shell窗口，可用于测试XPath语法

scrapy list # 查看爬虫列表

scrapy view [options] "www.example.com" # 查看下载的网页是否与目标网页一致

## 两个python的独特语法

yield与推导式

yield：

初学时可以简单理解为一种特殊的return方式

yield返回一个生成器对象，可以逐个的选择其中的元素，也可以直接将其转化成list对象

惰性求值：在真正需要的时候才进行相应的计算

推导式：

一种具有python特点的优雅的初始化语法

特殊：元组推导式，需要用tuple()进行类型转化