import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(4)
driver.maximize_window()
print(driver.title)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(4)
driver.get("https://www.youtube.com")
print(driver.title)
time.sleep(5)
y = driver.find_element(By.NAME,"search_query").send_keys("Prank on Family"+Keys.RETURN)
time.sleep(10)
print("Test ok")