from selenium import webdriver
import time

try:
    browser = webdriver.Chrome(executable_path='D:/driver/chromedriver.exe')
    time.sleep(1)

    browser.get(' https://shimo.im')

except:
    print()