import pytest
from PageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"


    def test_homePageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if(act_title=="Your store. Login"):
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if(act_title=="Dashboard / nopCommerce administratio"):
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False