# (e) Cut -> Copy -> Paste ->:
# ----------------------------
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver = webdriver.Edge()
driver.get("https://www.youtube.com")
driver.maximize_window()
time.sleep(6)
action = ActionChains(driver)
f=driver.find_element(By.ID, "search")
f.send_keys("2023 World Records")
time.sleep(5)
action.key_down(Keys.CONTROL).send_keys("a").perform()
time.sleep(5)
action.key_down(Keys.CONTROL).send_keys("x").perform() #Cut
time.sleep(5)
action.key_down(Keys.CONTROL).send_keys("c").perform() #Copy
t=driver.find_element(By.ID, "search")
action.click_and_hold(t).perform()
action.key_down(Keys.CONTROL).send_keys("v").perform()
time.sleep(5)
print("Test is Ok")