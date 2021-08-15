import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getPassword()
    logger=LogGen.logGeneration()

    @pytest.mark.regression
    def test_homePageTitle(self,setUp):
        self.logger.info("*********Test_001_Login******")
        self.logger.info("********Verifying home page title**********")
        self.driver=setUp
        self.driver.get(self.baseURL)
        actual_title=self.driver.title

        if actual_title=="Your store. Login":
            assert True
            self.driver.quit()
            self.logger.info("******** Home page title is PASSED **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"testhomepage.png")
            self.driver.quit()
            self.logger.error("******** Home page title is FAILED **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setUp):
        self.logger.info("*********Test_001_Login******")
        self.logger.info("********Verifying Valid Login**********")
        self.driver=setUp
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.quit()
            self.logger.info("******** Login is PASSED **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "testlogin.png")
            self.driver.quit()
            self.logger.error("******** Login is Failed **********")
            assert False

