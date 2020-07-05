from selenium import webdriver
import time

try:
    browser = webdriver.Chrome(executable_path='D:/driver/chromedriver.exe')
    time.sleep(1)

    browser.get(' https://shimo.im')
    btml = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]')
    btml.click()

    name = browser.find_element_by_name('mobileOrEmail')
    print(name)
    name.send_keys('XXXXXXXXX')
    time.sleep(1)
    browser.find_element_by_name('password').send_keys('XXXXXXXX')
    time.sleep(1)
    sinup = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')
    sinup.click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()