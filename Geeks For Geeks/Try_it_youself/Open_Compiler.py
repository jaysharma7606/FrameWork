import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/")
time.sleep(2)

# find the sigin button
driver.find_element(By.XPATH,"//*[@id='topMainHeader']/div/div/button").click()
time.sleep(2)

# enter the username
driver.find_element(By.XPATH,"//*[@id='login']/div/div[2]/div/div[3]/div[1]/input").send_keys("jay7055.ca23@chitkara.edu.in")
time.sleep(2)

# enter the password
driver.find_element(By.XPATH,"//*[@id='login']/div/div[2]/div/div[3]/div[2]/input").send_keys("Jaysharma@1234")
time.sleep(2)

# click to login
driver.find_element(By.XPATH,"//*[@id='login']/div/div[2]/div/div[3]/button").click()
time.sleep(2)

# click the tutorial
driver.find_element(By.XPATH,"//*[@id='comp']/div/div[1]/div/button/span").click()
time.sleep(10)

# click the problem solving buttton
practise=driver.find_element(By.XPATH,"//*[@id='topMainHeader']/div/ul/li[4]")

# move through mouse feature
a=ActionChains(driver)
a.move_to_element(practise).perform()
driver.implicitly_wait(10)

# click to solve the array problem
driver.find_element(By.XPATH,"//*[@id='topMainHeader']/div/ul/li[4]/ul/li[2]/a/a").click()
time.sleep(10)

# click to solve query option
driver.find_element(By.XPATH,'//*[@id="post-1324743"]/div[3]/div[2]/a[1]').click()
time.sleep(2)

# switch to new or next window
winds = driver.window_handles
parent = winds[0]
child = winds[1]
driver.switch_to.window(child)
driver.find_element(By.XPATH,"//*[@id='scrollableDiv']/div/div[1]/div[6]/div/div/div[1]/div/div[2]/button").click()
time.sleep(2)





# validate the script and check the test script was pass or fail
actual = driver.title
expected = 'Practice | GeeksforGeeks | A computer science portal for geeks'
if actual == expected:
    print("Test Case Passed")
else: print("Test Failed")
