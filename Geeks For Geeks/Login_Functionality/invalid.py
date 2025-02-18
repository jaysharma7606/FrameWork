import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='topMainHeader']/div/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='login']/div/div[2]/div/div[3]/div[1]/input").send_keys("jay7055.ca23@chitkara.edu.in")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='login']/div/div[2]/div/div[3]/div[2]/input").send_keys("Jaysharma@12")
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='login']/div/div[2]/div/div[3]/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='comp']/div/div[1]/div/button/span").click()
time.sleep(10)