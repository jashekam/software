from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='./Drivers/chromedriver.exe')

driver.get('http://www.google.com')

# Find the search box and enter a query
search_box = driver.find_element_by_xpath('//*[@id="APjFqb"]')
search_box.send_keys('selenium')
search_box.submit()

# Add a delay to keep the window open
time.sleep(10)

# Close the window and quit the driver
driver.close()
driver.quit()
