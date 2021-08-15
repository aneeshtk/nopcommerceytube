import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomer import SearchCustomer

class Test_SearchCustomerByRole_006:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGeneration()

    def test_searchCustomerByRole(self,setUp):
        self.logger.info("\n")
        self.logger.info("---- Test_SearchCustomerByRole_006 ----")
        self.driver=setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("--- User login is successful ---")

        self.logger.info("--- Starting search by Customer Role ---")
        self.addCust=AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerItemMenu()

        self.logger.info("---- Searching customer by Customer Role ---")
        self.searchcust=SearchCustomer(self.driver)
        self.searchcust.setCustomerRole("Administrators")
        self.searchcust.clickOnSearchButton()
        time.sleep(3)
        status=self.searchcust.searchCustomerByRole("Administrators")
        assert True==status
        self.driver.quit()
        self.logger.info("---- Test_SearchCustomerByRole_006 finished ---")
