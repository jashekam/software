from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='./Drivers/chromedriver.exe')

driver.get('http://www.google.com')

# Add a delay to keep the window open
time.sleep(10)

# Close the window and quit the driver
driver.close()
driver.quit()
