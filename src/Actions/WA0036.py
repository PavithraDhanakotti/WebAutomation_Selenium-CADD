# (b) Right Click:
# ----------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
time.sleep(3)
r=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/div/article/div/header/nav/div/span[3]/a")
time.sleep(3)
action=ActionChains(driver)
action.context_click(r).perform()
time.sleep(5)
r1=action.key_down(Keys.CONTROL).click()
print("Test Ok")