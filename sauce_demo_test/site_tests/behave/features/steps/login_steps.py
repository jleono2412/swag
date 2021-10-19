import time

from behave import given, when, then

from libraries.test_setup import EnvironmentSetup
from site_tests.behave.pages.login import LoginPage
from site_tests.behave.pages.products_page import ProductsPage


class LoginSteps(EnvironmentSetup):

    @given(u'I want to login in "{site}"')
    def i_want_to_login(context,site):
        EnvironmentSetup.setUp(context)
        context.driver.get(site)
        context.login = LoginPage(context.driver)

    @when(u'Enter the credentials')
    def enter_the_credentials(context):
        for row in context.table:
            context.user = row["user_name"]
            context.password = row["password"]
        context.login.type_user_name(context.user)
        context.login.type_password(context.password)
        context.login.click_on_login()

    @then(u'I enter in products section')
    def i_enter_in_products_section(context):
        context.products = ProductsPage(context.driver)
        context.products.products_section_exist()

    @then(u'Error message must be appear')
    def error_message_must_be_appear(context):
        for row in context.table:
            context.error_message = row["error_message"]
        context.login.check_message_error(context.error_message)