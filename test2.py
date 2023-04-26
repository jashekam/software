from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='./Drivers/chromedriver.exe')
driver.get('https://google.com')
#search_box = driver.find_element_by_xpath('//*[@id="APjFqb"]')
time.sleep(100)
