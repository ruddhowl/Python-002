from fake_useragent import UserAgent
import requests
from lxml import etree

ua = UserAgent(verify_ssl = False)
headers = {
    'User-Agent' : ua.random,
    # 'Referer' :  'https://shimo.im/login?from=home '
}
# url = 'https://shimo.im'
# r = requests.get(url, headers = headers)
# print(r.status_code)
# print(r.text)
# with open('shimo.html', 'w', encoding='utf-8') as h:
#     h.write(r.text)
# login_url = 'https://shimo.im/login?from=home'
# r = requests.get(login_url, headers = headers)
# with open('shimo_login.html', 'w', encoding='utf-8') as l:
#     l.write(r.text)

with open('shimo_login.html', 'r', encoding='utf-8') as l:
    html = l.read()
# 网页经过加密处理，所以解析不了
s = etree.HTML(html)
# //*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input
tmp = s.xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/label')
print(tmp)