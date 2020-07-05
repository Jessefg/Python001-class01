from selenium import webdriver
import time

"""
1. 使用 requests 或 Selenium 
2. 模拟登录石墨文档 https://shimo.im
"""


try:
    url = 'https://shimo.im'
    web = webdriver.Chrome()
    web.get(url)

    time.sleep(3)

    # 登陆按钮
    web.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]').click()

    time.sleep(3)

    # 输入密码
    web.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('username')
    web.find_element_by_xpath('//*[@name="password"]').send_keys('password')

    time.sleep(3)
    web.find_element_by_xpath('//*[@class="form-wrapper"]/div/div/button').click()

    print(web.get_cookies())


except Exception as ex:
    print(ex)
