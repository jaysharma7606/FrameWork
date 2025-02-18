import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='comp']/div[2]/div[1]/div[2]/input").send_keys("HTML Tutorial")
driver.find_element(By.XPATH,"//*[@id='comp']/div[2]/div[1]/div[2]/span").click()
time.sleep(20)