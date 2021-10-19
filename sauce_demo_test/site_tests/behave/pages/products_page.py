import time

from selenium.webdriver.common.by import By

from libraries import locators, forms, mouse
from libraries.test_setup import EnvironmentSetup


class ProductsPage(EnvironmentSetup):

    def __init__(self,driver):
        self.driver = driver
        self.products_list = "//div[@id='inventory_container']/div[@class='inventory_list']//div[@class='inventory_item_']"
        self.name_products = "//div[@id='inventory_container']/div[@class='inventory_list']//div[@class='inventory_item']//div[@class='inventory_item_name']"
        self.add_cart_btns = "//div[@id='inventory_container']/div[@class='inventory_list']//div[@class='inventory_item']//div[@class='pricebar']/button"
        self.inventory_list = "//div[@id='inventory_container']/div[@class='inventory_list']"
        self.products_span = "//span[contains(text(),'Products')]"
        self.cart_icon = "//div[@id='header_container']//a[@class='shopping_cart_link']"

    def products_section_exist(self):
        self.assertTrue(locators.element_exists(self,"XPATH",self.products_span) == True,"section doesn't exist")

    def click_on_products_cart(self):
        mouse.click_on_element(self,"XPATH",self.cart_icon)
        time.sleep(10)

    def find_products(self,product_name):
        self.names_of_products = []
        if len(product_name.split(","))>0:
            self.names_of_products = product_name.split(",")
        else:
            self.names_of_products = product_name
        self.product_names = []
        self.add_cart_btns_list = []
        self.inventory_list = locators.element_located(self,"XPATH",self.inventory_list)
        self.product_names = self.inventory_list.find_elements(By.XPATH,self.name_products)
        self.add_cart_btns_list = self.inventory_list.find_elements(By.XPATH,self.add_cart_btns)
        if len(self.names_of_products)>0:
            for j in range (0,len(self.names_of_products)):
                for i in range(0,len(self.product_names)):
                    if self.names_of_products[j] == self.product_names[i].text:
                        self.add_cart_btns_list[i].click()
                        time.sleep(4)
        else:
            for i in range(0, len(self.product_names)):
                if self.names_of_products[0] == self.product_names[i].text:
                    self.add_cart_btns_list[i].click()
                    time.sleep(4)