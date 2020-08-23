from selenium import webdriver
import time

try:
    browser = webdriver.Chrome(executable_path='D:/driver/chromedriver.exe')
    time.sleep(1)

    browser.get(' https://shimo.im')
    btml = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]')
    btml.c

except:
    print('finish')
finally:
    browser.close()