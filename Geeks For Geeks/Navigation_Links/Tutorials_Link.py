import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='secondarySubHeader']/ul/li[3]/a").click()
time.sleep(20)