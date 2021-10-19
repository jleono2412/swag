import time
from selenium.webdriver.common.action_chains import ActionChains


# ---------------
# Mouse Functions
# ---------------
from libraries import locators


def click_on_element(self, locator_type, locator):

    element = locators.element_clickeable(self, locator_type, locator)
    element.click()


def click_action_on_element(self, locator_type, locator, times=1):
    element = locators.locator_element(self, locator_type, locator)
    locators.highlight(self, element)
    for i in range(times):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()

def click_js_on_element(self, locator_type, locator):
    element = locators.locator_element(self, locator_type, locator)
    self.driver.execute_script("arguments[0].click();", element)


def double_click_on_element(self, locator_type, locator):
    time.sleep(0.5)
    element = locators.locator_element(self, locator_type, locator)
    locators.highlight(self, element)
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()