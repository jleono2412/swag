import time

from selenium.webdriver.common.by import By

from libraries import locators
from libraries.test_setup import EnvironmentSetup


class RemoveProducts(EnvironmentSetup):

        def __init__(self,driver):
            self.driver = driver
            self.list_of_added_products = "//div[@class='cart_list']/div[@class='cart_item']"
            self.name_products_added = "//div[@class='cart_list']/div[@class='cart_item']//div[@class='inventory_item_name']"
            self.name_products_added = "//div[@class='cart_list']/div[@class='cart_item']//button"

        def find_products_to_remove(self,products_to_remove):
             self.names_of_products_to_remove = []
             if len(products_to_remove.split(","))>0:
                self.names_of_products_to_remove = products_to_remove.split(",")
             else:
              self.names_of_products_to_remove = products_to_remove
              self.product_names_to_remove = []
              self.remove_cart_btns_list = []
              self.inventory_list = locators.element_located(self,"XPATH",self.list_of_added_products)
              self.product_names_to_remove = self.inventory_list.find_elements(By.XPATH,self.name_products_added)
              self.remove_cart_btns_list = self.inventory_list.find_elements(By.XPATH,self.name_products_added)
              if len(self.names_of_products_to_remove)>0:
                for j in range (0,len(self.names_of_products_to_remove)):
                    for i in range(0,len(self.product_names_to_remove)):
                        if self.names_of_products_to_remove[j] == self.product_names_to_remove[i].text:
                            self.remove_cart_btns_list[i].click()
                            time.sleep(4)
              else:
                for i in range(0, len(self.product_names_to_remove)):
                    if self.names_of_products_to_remove[0] == self.product_names_to_remove[i].text:
                        self.remove_cart_btns_list[i].click()
                        time.sleep(4)

