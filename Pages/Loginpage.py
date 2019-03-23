#from selenium import webdriver
import time
class loginpage():
    def __init__(self,driver):
        self.driver=driver
        self.username_textbox_id='email'
        self.password_textbox_id='password'
        self.login_button_id='submit_button'
    ####### HOME PAGE OBJECTS ######
        self.name_link_xpath='//div[@class="username"]'
        self.logout_link_xpath='//i[@class="fa fa-sign-out"]'


    def enter_email(self,email):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        time.sleep(3)
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(email)
    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        time.sleep(3)
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
####### HOME PAGE FUNCTIONS ######
