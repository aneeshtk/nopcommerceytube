from selenium.webdriver.support.ui import Select
import time
class AddCustomer:
#locators
    _linkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    _linkCustomer_menuItem_xpath="//a[@class='nav-link']//p[text()=' Customers']"
    _button_addNew_xpath = "//a[@class='btn btn-primary']"
    _textbox_email_xpath="//input[@id='Email']"
    _textbox_password_xpath="//input[@id='Password']"
    _textbox_firstName_xpath="//input[@id='FirstName']"
    _textbox_lastName_xpath="//input[@id='LastName']"
    _radiobutton_male_xpath="//input[@id='Gender_Male']"
    _radiobutton_female_xpath="//input[@id='Gender_Female']"
    _textbox_company_xpath="//input[@id='Company']"
    _checkbox_isTaxExempt_xpath="//input[@id='IsTaxExempt']"
    _list_newsLetter_xpath="//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div/div[1]/div"
    _listItem_yourStoreName="//li[contains(text(),'Your store name')]"
    _list_customerRoles_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"

    _listItem_administrators_xpath="//li[contains(text(),'Administrators')]"
    _listItem_guests_xpath="//li[contains(text(),'Guests')]"
    _listItem_vendors_xpath="//li[contains(text(),'Vendors')]"
    _listItem_registered_xpath="//li[contains(text(),'Registered')]"
    _dropdown_vendorManager_xpath="//*[@id='VendorId']"
    _textbox_dateOfBirth_xpath="//input[@id='DateOfBirth']"
    _textarea_adminContent_xpath="//textarea[@id='AdminComment']"
    _button_save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self._linkCustomers_menu_xpath).click()

    def clickOnCustomerItemMenu(self):
        self.driver.find_element_by_xpath(self._linkCustomer_menuItem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self._button_addNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self._textbox_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self._textbox_password_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element_by_xpath(self._textbox_firstName_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element_by_xpath(self._textbox_lastName_xpath).send_keys(lastname)

    def setCustomerRole(self,role):

        self.driver.find_element_by_xpath(self._list_customerRoles_xpath).click()
        time.sleep(3)
        if role=="Registered":
            self.listItem=self.driver.find_element_by_xpath(self._listItem_registered_xpath)
        elif role=="Administrators":
            self.listItem = self.driver.find_element_by_xpath(self._listItem_administrators_xpath)
        elif role=="Vendors":
            self.listItem = self.driver.find_element_by_xpath(self._listItem_vendors_xpath)
        elif role=="Guests":
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listItem = self.driver.find_element_by_xpath(self._listItem_guests_xpath)
        else:
            self.listItem = self.driver.find_element_by_xpath(self._listItem_guests_xpath)
        time.sleep(2)
        #direct click on the elements is not working so we have used execute_script method
        self.driver.execute_script("arguments[0].click();",self.listItem)

    def setManagerRole(self,value):
        drp=Select(self.driver.find_element_by_xpath(self._dropdown_vendorManager_xpath))
        drp.select_by_visible_text(value)
    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element_by_xpath(self._radiobutton_male_xpath).click()
        elif gender=="Female":
            self.driver.find_element_by_xpath(self._radiobutton_female_xpath).click()
        else:
            self.driver.find_element_by_xpath(self._radiobutton_male_xpath).click()

    def setDateOfBirth(self,dob):
        self.driver.find_element_by_xpath(self._textbox_dateOfBirth_xpath).send_keys(dob)

    def setCompanyName(self,company):
        self.driver.find_element_by_xpath(self._textbox_company_xpath).send_keys(company)

    def setAdminContent(self,content):
        self.driver.find_element_by_xpath(self._textarea_adminContent_xpath).send_keys(content)

    def clickOnSaveButton(self):
        self.driver.find_element_by_xpath(self._button_save_xpath).click()











