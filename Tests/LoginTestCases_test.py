import time

import pytest

from Pages.Homepage import homepage
from Pages.Loginpage import loginpage
from Utils import readexcel
from Utils import utils as utils


#@pytest.mark.usefixtures('setup')
class Testlogin():

    @pytest.mark.parametrize('email,password', readexcel.read_data())
    def test_login(self, email,password):
        driver = self.driver
        driver.get(utils.url)
        login = loginpage(driver)
        login.enter_email(email)
        login.enter_password(password)
        login.click_login()
        time.sleep(2)
        home = homepage(driver)
        home.click_name()
        time.sleep(2)
        home.logout_link()
        time.sleep(2)
