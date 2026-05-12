from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import WebDriverWait


driver=webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

wait=WebDriverWait(driver,10)

username=driver.find_element(By.ID,"username")

username.send_keys("tomsmith")

password=driver.find_element(By.ID,"password")

password.send_keys("SuperSecretPassword!")

password.send_keys(Keys.ENTER)



message=driver.find_element(By.TAG_NAME,"h4")

text=message.text

if text=="Welcome to the Secure Area. When you are done click logout below.":
    print("test successful ...")
else:
    print("test failed")

button=driver.find_element(By.LINK_TEXT,"Logout")
button.click()
print('logged out from the site')




