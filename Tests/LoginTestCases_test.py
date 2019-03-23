import pytest
from Pages.Homepage import homepage
from Pages.Loginpage import loginpage
from Utils import utils as utils
from Utils import readexcel
import time



@pytest.mark.usefixtures('setup')

class Testlogin():
    @pytest.mark.parametrize('data',readexcel.read_data())
    def test_login(self,data):
        driver=self.driver
        driver.get(utils.url)
        login=loginpage(driver)
        login.enter_email(data[0])
        login.enter_password(data[1])
        login.click_login()
        time.sleep(2)
        home=homepage(driver)
        home.click_name()
        time.sleep(2)
        home.logout_link()
        time.sleep(3)



