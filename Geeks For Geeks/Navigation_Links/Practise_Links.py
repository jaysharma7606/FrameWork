import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
time.sleep(2)
practise=driver.find_element(By.XPATH,"//*[@id='topMainHeader']/div/ul/li[4]")
a=ActionChains(driver)
a.move_to_element(practise).perform()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//*[@id='topMainHeader']/div/ul/li[4]/ul/li[2]/a/a").click()
time.sleep(20)