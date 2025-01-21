from selenium import webdriver
from pom


class TestLogin:
    def test_login(self):
        driver=webdriver.Chrome()
        driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
        driver.implicitly_wait(10)
        driver.maximize_window()
        lp = LoginPage(driver)
        lp.setUserName("jaysharma@gmail.com")
        lp.setPassword("123456")
        lp.setbtn()
        act_title = driver.title
        assert act_title == "My account - My Shop"