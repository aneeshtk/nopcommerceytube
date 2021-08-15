import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random
import string

class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getPassword()
    logger=LogGen.logGeneration()

    @pytest.mark.sanity
    def test_addCustomer(self,setUp):
        self.logger.info("****** Test_003 AddCustomer ******")
        self.driver=setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** Login Successful for add customer ********")
        self.logger.info("***** Add customer test method starts ******")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerItemMenu()
        self.addcust.clickOnAddNew()

        self.logger.info("**** Providing Customer information *****")
        self.email=random_generator()+"@testemail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("tesuser001")
        self.addcust.setFirstName("Test")
        self.addcust.setLastName("User_001")
        self.addcust.setGender("Male")
        self.addcust.setDateOfBirth("07/05/1990")
        self.addcust.setCustomerRole("Guests")
        self.addcust.setCompanyName("Test Company")
        self.addcust.setManagerRole("Vendor 2")
        self.addcust.setAdminContent("This user is created for testing")
        self.addcust.clickOnSaveButton()
        self.logger.info("** Saving customer Information **")

        self.msg=self.driver.find_element_by_tag_name("body").text

        if 'The new customer has been added successfully.' in self.msg:
            assert True==True
            self.logger.info("******** Add Customer Test Passed************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addcustomer_scr.png")
            self.logger.error("** Add Customer Test is failed **")
            assert True==False

        self.driver.quit()
        self.logger.info("** End of Add Customer Test **")



#create random data with size 8 with all lowercase letters
def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))