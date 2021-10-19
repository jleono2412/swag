import time

from libraries import forms, mouse, locators
from libraries.test_setup import EnvironmentSetup


class LoginPage(EnvironmentSetup):

    def __init__(self,driver):

        self.driver= driver
        self.user_name_txt = "//input[@id='user-name']"
        self.password_txt = "//input[@id='password']"
        self.login_btn = "//input[@id='login-button']"

        self.error_msj = "//body/div[@id='root']//div/h3"


    def type_user_name(self,user_name):
        forms.enter_text_on_element(self, "XPATH", self.user_name_txt, user_name)

    def type_password(self,password):
        forms.enter_text_on_element(self, "XPATH", self.password_txt, password)

    def click_on_login(self):
        mouse.click_on_element(self, "XPATH", self.login_btn)



    def check_message_error(self,error_message):
        print(locators.element_located(self,"XPATH",self.error_msj).text)
        self.assertTrue(error_message == locators.element_located(self,"XPATH",self.error_msj).text,"unexpected error message")
