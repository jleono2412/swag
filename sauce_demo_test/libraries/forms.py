
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# -----------------
# Text functions
# -----------------
from libraries import locators
from libraries import mouse


def enter_text_on_element(self,locator_type, locator, value):
    #time.sleep(0.5)
    element = locators.element_located(self, locator_type, locator)
    #element = locators.locator_element(self, locator_type, locator)
#    locators.highlight(self, element)
    element.clear()
    element.send_keys(value)


def enter_text_press_enter(self, locator_type, locator, value):
    #time.sleep(0.5)
    element = locators.element_located(self, locator_type, locator)
    #element = locators.locator_element(self, locator_type, locator)
    locators.highlight(self, element)
    element.clear()
    element.send_keys(value, Keys.ENTER)


def enter_text_press_enter_and_tab(self, locator_type, locator, value):
    #time.sleep(0.5)
    #element = locators.locator_element(self, locator_type, locator)
    element = locators.element_located(self, locator_type, locator)
    locators.highlight(self, element)
    element.send_keys(value, Keys.ENTER)
    element.send_keys(value, Keys.TAB)


def get_text_on_element(self, locator_type, locator):
    #time.sleep(0.5)
    #element = locators.locator_element(self, locator_type, locator)
    element = locators.element_located(self, locator_type, locator)
    #locators.highlight(self, element)
    return element.text


# def get_input_text(self, locator_type, locator):
#     element = locators.locator_element(self, locator_type, locator)
#     return element.get_attribute('value')

def press_enter(self, locator_type, locator):
    element = locators.locator_element(self, locator_type, locator)
    element.send_keys(Keys.ENTER)

# ------------------
# Tables driving
# ------------------


def get_information_of_table_columns(self, list_columns, generic_xpath):
    xpaths_columns = []
    columns_driver = []
    columns_list_with_information = []
    for number_column in list_columns:
        xpaths_columns.append(generic_xpath + "[" + str(number_column) + "]")
    for xpath_column in xpaths_columns :
        column = self.driver.find_elements_by_xpath(xpath_column)
        columns_driver.append(column)
    for column_driver in columns_driver:
        data_columns = []
        for position in range(len(column_driver)):
            data_columns.append(column_driver[position].text)
        columns_list_with_information.append(data_columns)
    return columns_list_with_information


# ------------------
# Checkbox functions
# ------------------

def check_checkbox(self, locator_type, locator):
    """Check a checkbox if this is not checked"""
    is_checked = locators.get_attribute_value(self, locator_type, locator, 'checked')
    if not is_checked:
        mouse.click_on_element(self, locator_type, locator)


def uncheck_checkbox(self, locator_type, locator):
    """Uncheck a checkbox if this is checked"""
    is_checked = locators.get_attribute_value(self, locator_type, locator, 'checked')
    if is_checked:
        mouse.click_on_element(self, locator_type, locator)


# ------------------
# Dropdown functions
# ------------------

def select_option_by_value(self, locator_type, locator, value):
    Select(locators.locator_element(self, locator_type, locator)).select_by_value(value)


def select_option_by_index(self, locator_type, locator, index):
    Select(locators.locator_element(self, locator_type, locator)).select_by_index(index)


def select_option_by_text(self, locator_type, locator, text):
    Select(locators.locator_element(self, locator_type, locator)).select_by_visible_text(text)




