# (a) Webdriver Exception:
# ------------------------
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.maximize_window()
time.sleep(5)
try:
    driver.get("https://www.walmarting.com/")
    d=driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/span/header/form/div/input")
    d.click()
except WebDriverException:
    print("Please Check The Web Address")
    time.sleep(3)
print("Test OK")