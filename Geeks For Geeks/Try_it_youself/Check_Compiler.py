import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/ide/online-cpp14-compiler")
time.sleep(2)

driver.find_element(By.ID,"runButton").click()
time.sleep(10)
