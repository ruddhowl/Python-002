# This test is failed.
from fake_useragent import UserAgent
import requests

ua = UserAgent(verify_ssl = False)
headers = {
    'User-Agent' : ua.random,
    # 'Referer' :  'https://shimo.im/login?from=home '
}

s = requests.Session()
# Session对象：在同一个 Session实例发出的所有请求之间保持cookie， 
login_url = 'https://shimo.im/login?from=home'
form_data = {
    'mobile' : '+86xxxxxxxxxx',
    'password' : 'xxxxxxx'
}

# post登陆信息之前先获取cookie
# pre_login = 'https://shimo.im'
# pre_resp = s.get(pre_login, headers = headers)
# print(pre_resp.status_code)

response = s.post(login_url, data = form_data, headers = headers, cookies = s.cookies)
print(response.status_code)
