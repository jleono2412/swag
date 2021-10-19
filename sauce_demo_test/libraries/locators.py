import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# -----------------
# Locator functions
# -----------------


def element_clickeable(self, by, what):
    all_by= locator_element_test(by)
    element = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((all_by, what)))
    return element

def element_located(self,by, what):
    all_by = locator_element_test(by)
    element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((all_by,what)))
    return element


def locator_element_test(locator_type):
    """Find an element and return it"""
    time.sleep(0.5)
    if str(locator_type).upper() == 'ID':
        by = By.ID
    elif str(locator_type).upper() == 'NAME':
        by = By.NAME
    elif str(locator_type).upper() == 'XPATH':
        by = By.XPATH
    elif str(locator_type).upper() == 'CSS':
        by = By.CSS_SELECTOR
    elif str(locator_type).upper() == 'LINK':
        by = By.LINK_TEXT
    elif str(locator_type).upper() == 'CLASS_NAME':
        by = By.CLASS_NAME
    return  by

def locator_elements(self, locator_type, locator):
    """Find set of elements and return them"""
    time.sleep(0.5)
    if str(locator_type).upper() == 'ID':
        by = By.ID
    elif str(locator_type).upper() == 'NAME':
        by = By.NAME
    elif str(locator_type).upper() == 'XPATH':
        by = By.XPATH
    elif str(locator_type).upper() == 'CSS':
        by = By.CSS_SELECTOR
    elif str(locator_type).upper() == 'LINK':
        by = By.LINK_TEXT
    elif str(locator_type).upper() == 'CLASS_NAME':
        by = By.CLASS_NAME
    return self.driver.find_elements(by, locator)

def locator_elements(self, locator_type, locator):
    """Find set of elements and return them"""
    time.sleep(0.5)
    if str(locator_type).upper() == 'ID':
        by = By.ID
    elif str(locator_type).upper() == 'NAME':
        by = By.NAME
    elif str(locator_type).upper() == 'XPATH':
        by = By.XPATH
    elif str(locator_type).upper() == 'CSS':
        by = By.CSS_SELECTOR
    elif str(locator_type).upper() == 'LINK':
        by = By.LINK_TEXT
    elif str(locator_type).upper() == 'CLASS_NAME':
        by = By.CLASS_NAME
    return self.driver.find_elements(by, locator)

def element_exists(self, locator_type, locator):

    element = locator_elements(self,locator_type,locator)
    if len(element) > 0:
        return True
    else:
        return False



def highlight(self, element):
    """Highlights (blinks) a Selenium Webdriver element"""
    try:
        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(0.3)
        apply_style(original_style)
    except:
        return
# ----------------------------------
# Attributes and properties functions
# ----------------------------------


# def get_attribute_value(self, locator_type, locator, attribute):
#     element = element_located(self, locator_type, locator)
#     attribute_value = element.get_attribute(attribute)
#     return attribute_value
#
#
# def get_all_attributes(self, locator_type, locator):
#     element = element_located(self, locator_type, locator)
#     attrs = []
#     for attr in element.get_property('attributes'):
#         attrs.append([attr['name'], attr['value']])
#     return attrs