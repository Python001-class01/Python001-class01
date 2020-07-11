
#这个模拟登陆，我是以前学过，但是xpath 不熟悉，为了怕被网站发现，多sleep
#拿到cookies ，注意它也是有时效的
#拿来主义，但我看了代码，

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html

    browser.get('https://shimo.im')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@class="login-button btn_hover_style_8"]').click()
    time.sleep(2)
    # browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])

    browser.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('18812345678')
    browser.find_element_by_xpath('//*[@name="password"]').send_keys('12345678')
    time.sleep(1)
    bt = browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]')
    time.sleep(1)
    bt.click()
    cookies = browser.get_cookies() # 获取cookies
    print(cookies)
    time.sleep(5)

except Exception as e:
    print(e)
finally:
    browser.close()
