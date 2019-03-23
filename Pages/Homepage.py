class homepage():

    def __init__(self,driver):
        self.driver=driver
        self.name_link_xpath='//div[@class="username"]'
        self.logout_link_xpath='//i[@class="fa fa-sign-out"]'



    def click_name(self):
        self.driver.find_element_by_xpath(self.name_link_xpath).click()

    def logout_link(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()

