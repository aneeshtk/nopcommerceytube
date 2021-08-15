from selenium import  webdriver
import pytest
@pytest.fixture()
def setUp(browser):
    chrome_path = "D:\\Selenium\\Projects\\nopcommerceytube\\drivers\\chromedriver.exe"
    firefox_path = "D:\\Selenium\\Projects\\nopcommerceytube\\drivers\\geckodriver.exe"
    ie_path = "D:\\Selenium\\Projects\\nopcommerceytube\\drivers\\IEDriverServer.exe"
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path=chrome_path)
        print("Launching chrome browser")
    elif browser=='firefox':
        driver=webdriver.Firefox(executable_path=firefox_path)
        print("Launching Firefox browser")

    else:
        driver=webdriver.Ie(executable_path=ie_path)
        print("Launching IE browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#### Pytest HTML Reports ########

def pytest_configure(config):
    config._metadata['Project Name']='NOP Commerce Ytube'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester Name']='Aneesh'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
