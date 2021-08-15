import time
class SearchCustomer:
    _text_email_id="SearchEmail"
    _text_company_id="SearchCompany"
    _text_firstname_id="SearchFirstName"
    _text_lastname_id="SearchLastName"
    _button_search_id="search-customers"

    _div_table_xpath="//div[@class='dataTables_scroll']"

    _table_searchresults_xpath="//table[@id='customers-grid']"
    _table_rows_xpath="//table[@id='customers-grid']//tbody//tr"
    _table_columns_xpath="//table[@id='customers-grid']//tbody//tr//td"

    _list_customerrole_xpath="/html/body/div[3]/div[1]/form[1]/section/div/div/div/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div"
    _button_customerclose_xpath="//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]"

    _listItem_administrators_xpath="//li[contains(text(),'Administrators')]"
    _listItem_forumMod_xpath = "//li[contains(text(),'Forum Moderators')]"
    _listItem_guest_xpath = "//li[contains(text(),'Guests)]"
    _listItem_registered_xpath = "//li[contains(text(),'Registered')]"
    _listItem_vendor_xpath = "//li[contains(text(),'Vendors')]"


    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self._text_email_id).clear()
        self.driver.find_element_by_id(self._text_email_id).send_keys(email)

    def setFirstName(self,firstname):
        self.driver.find_element_by_id(self._text_firstname_id).clear()
        self.driver.find_element_by_id(self._text_firstname_id).send_keys(firstname)
    def setLastName(self,lastname):
        self.driver.find_element_by_id(self._text_lastname_id).clear()
        self.driver.find_element_by_id(self._text_lastname_id).send_keys(lastname)

    def setCompany(self,company):
        self.driver.find_element_by_id(self._text_company_id).clear()
        self.driver.find_element_by_id(self._text_company_id).send_keys(company)

    def clickOnSearchButton(self):
        self.driver.find_element_by_id(self._button_search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self._table_rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self._table_columns_xpath))


    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element_by_xpath(self._div_table_xpath)
            emailId=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailId==email:
                flag = True
                break
        return flag

    def searchCustomerByName(self,name):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element_by_xpath(self._div_table_xpath)
            record_name=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if record_name==name:
                flag = True
                break
        return flag

    def setCustomerRole(self,customerRole):
        self.driver.find_element_by_xpath(self._button_customerclose_xpath).click()
        self.driver.find_element_by_xpath(self._list_customerrole_xpath).click()
        time.sleep(3)

        if customerRole=="Registered":
            self.listItem=self.driver.find_element_by_xpath(self._listItem_registered_xpath)
        elif customerRole=="Administrators":
            self.listItem = self.driver.find_element_by_xpath(self._listItem_administrators_xpath)
        elif customerRole=="Vendors":
            self.listItem = self.driver.find_element_by_xpath(self._listItem_vendors_xpath)
        elif customerRole=="Guests":
            self.listItem = self.driver.find_element_by_xpath(self._listItem_guests_xpath)
        else:
            self.listItem = self.driver.find_element_by_xpath(self._listItem_guests_xpath)
        time.sleep(2)
        #direct click on the elements is not working so we have used execute_script method
        self.driver.execute_script("arguments[0].click();",self.listItem)

    def searchCustomerByRole(self, role):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self._div_table_xpath)
            record_name = table.find_element_by_xpath(
                    "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[4]").text
            if role in record_name:
                flag = True
                break
        return flag
