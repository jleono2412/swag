import time

from behave import when

from libraries.test_setup import EnvironmentSetup
from site_tests.behave.pages.products_page import ProductsPage
from site_tests.behave.pages.remove_products_page import RemoveProducts


class ProductsSteps(EnvironmentSetup):

    @when(u'I want to add products to the cart list')
    def i_want_to_add_products_to_the_cart_list(context):
        context.product_list = ProductsPage(context.driver)
        for row in context.table:
            context.product = row["products"]
        context.producr_list.find_products(context.product)

    @when(u'I want to remove products to the cart list')
    def i_want_to_remove_products_to_the_cart_list(context):
        context.product_list = ProductsPage(context.driver)
        context.product_list.click_on_products_cart()
        for row in context.table:
            context.product = row["products"]
        context.remove_products =RemoveProducts(context.driver)
        context.remove_products.find_products_to_remove(context.product)