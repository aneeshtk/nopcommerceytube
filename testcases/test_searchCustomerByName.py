import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomer import SearchCustomer
class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGeneration()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setUp):
        self.logger.info("---- Test_SearchCustomerByName_005 ----")
        self.driver=setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("--- User login is successful ---")

        self.logger.info("--- Starting search by Name ---")
        self.addCust=AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerItemMenu()

        self.logger.info("---- Searching customer by name ---")
        self.searchcust=SearchCustomer(self.driver)
        self.searchcust.setFirstName("Victoria")
        self.searchcust.setLastName("Terces")
        self.searchcust.clickOnSearchButton()
        time.sleep(5)
        status=self.searchcust.searchCustomerByName("Victoria Terces")
        assert True==status
        self.driver.quit()
        self.logger.info("---- Test_SearchCustomerByName_005 finished ---")
