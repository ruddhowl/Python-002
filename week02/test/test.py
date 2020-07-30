# from fake_useragent import UserAgent
# import requests
# from lxml import etree

# ua = UserAgent(verify_ssl = False)
# headers = {
#     'User-Agent' : ua.random,
#     # 'Referer' :  'https://shimo.im/login?from=home '
# }
# # url = 'https://shimo.im'
# # r = requests.get(url, headers = headers)
# # print(r.status_code)
# # print(r.text)
# # with open('shimo.html', 'w', encoding='utf-8') as h:
# #     h.write(r.text)
# # login_url = 'https://shimo.im/login?from=home'
# # r = requests.get(login_url, headers = headers)
# # with open('shimo_login.html', 'w', encoding='utf-8') as l:
# #     l.write(r.text)

# with open('shimo_login.html', 'r', encoding='utf-8') as l:
#     html = l.read()
# # 网页经过加密处理，所以解析不了
# s = etree.HTML(html)
# # //*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input
# tmp = s.xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/label')
# print(tmp)




# 导入第三方库
# requests用来获取网页
import requests
from lxml import etree

with open('maoyan.html', 'r') as f:
    text = f.read()

s = etree.HTML(text).xpath('//div[@class="movie-hover-info"]')
# s = etree.HTML(text).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]')
print(type(s))  
print(s[1])
r = s[1].xpath(f'./div[4]/text()')
# //*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[1]/div[2]/a/div/div[1]/span
print(r)
