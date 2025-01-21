from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    txt_email_id = 'email'
    txt_password = 'passwd'
    btn_sigin = 'SubmitLogin'

    def __init__(self,driver):
        self.driver=driver
    def setUserName(self,username):
        usertxt = self.driver.find_element(By.ID,self.txt_email_id)
        usertxt.send_keys(username)

    def setPassword(self,password):
        usertxt = self.driver.find_element(By.ID,self.txt_password)
        usertxt.send_keys(password)

    def setbtn(self):
        btn = self.driver.find_element(By.ID,self.btn_sigin)
        btn.click()