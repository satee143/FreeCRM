from selenium import webdriver
import pytest
import time
def pytest_addoption(parser):
     parser.addoption('--browser',action='store',default='chrome')

@pytest.fixture(scope='class')
def setup(request):
    try:

        browser=request.config.getoption('--browser')
        if browser=='chrome':
             driver=webdriver.Chrome(executable_path='c:/Users/Dusa/PycharmProjects/FreeCRM/Drivers/chromedriver.exe')
        elif browser=='firefox':
             driver=webdriver.Firefox(executable_path='c:/Users/Dusa/PycharmProjects/FreeCRM/Drivers/geckodriver.exe')
        driver.maximize_window()
        driver.implicitly_wait(3)
        request.cls.driver=driver
        time.sleep(3)
        yield
        driver.close()
        driver.quit()

    except:
        print('Error at Conftest File')