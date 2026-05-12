from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://www.google.com")

text_area=driver.find_element(By.NAME,"q")
text_area.send_keys("grey jacket")
text_area.send_keys(Keys.ENTER)
# text_area.submit()



time.sleep(10)
driver.quit()

