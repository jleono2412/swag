import os
import unittest

from selenium import webdriver
import chromedriver_binary

class EnvironmentSetup(unittest.TestCase):

    def setUp(self):
        self.path = get_path_driver(self)
        self.driver = webdriver.Chrome(self.path)
        self.driver.maximize_window()

def tearDown(self):
    self.driver.quit()


def get_path_driver(self):
    self.path_to_cut = os.getcwd()
    self.temp1 = self.path_to_cut.find("test/")
    if self.temp1 != -1:
        self.temp1 = self.path_to_cut.find("test") + 10
        self.length = len(self.path_to_cut)
        self.path = self.path_to_cut[self.temp1:self.legth]
        self.path_driver = self.path_to_cut.replace(self.path, "Drivers/chromedriver")
        return self.path_driver
    else:
        path_behave = self.path_to_cut + "/Drivers/chromedriver"

    print(path_behave)
    return path_behave



if __name__ == '__main__':
    unittest.main()
