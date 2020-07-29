from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    
    browser.get('https://shimo.im/welcome')
    time.sleep(3)

    btm1 = browser.find_element_by_xpath("//div[@class='entries']/a[2]/button")
    btm1.click()
    time.sleep(3)
    
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('xxxxxxxxxx')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('xxxxxxxxxx')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(10)

except Exception as e:
    print(e)
finally:    
    browser.close() 