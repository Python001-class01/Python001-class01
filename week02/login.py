from selenium import webdriver
import time

# 成功配置了环境变量，依然报错
# 可以在初始化browser实例时，用绝对路径来调用chromedriver
browser = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe')
try:

    browser.get('https://shimo.im/welcome')
    time.sleep(3)

    # 利用浏览器直接复制xpath
    btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    btm1.click()

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('18106957306')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('960118')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()

