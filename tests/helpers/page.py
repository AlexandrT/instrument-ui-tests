from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from .locators import *
from .elements import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_region_link(self):
        element = self.driver.find_element(*BasePageLocators.REGION_LINK)
        return element

    def click_region(self):
        element = self.get_region_link()
        element.click()

    def get_cities_links(self):
        elements = self.driver.find_elements(*BasePageLocators.CITY_LINK)
        return elements

    def get_cities_with_delivery_links(self):
        elements = self.driver.find_elements(*BasePageLocators.CITY_WITH_DELIVERY_LINK)
        return elements

class MainPage(BasePage):
    pass

class ProductPage(BasePage):
    def click_sale_button(self):
        element = self.driver.find_element(*ProductPageLocators.ADD_BY_SALE_BUTTON)
        element.click()

    def get_saled_price(self):
        element = self.driver.find_element(*ProductPageLocators.SALED_PRICE)
        return element

    def get_price_after_adding(self):
        element = self.driver.find_element(*ProductPageLocators.COST_FROM_MODAL)
        return element

class ProductsListPage(BasePage):
    def get_product_with_bonuses(self):
        try:
            element = self.driver.find_element(*ProductsListPageLocators.PRODUCT_WITH_BONUSES)
        except NoSuchElementException:
            element = None
        return element

    def click_load_more(self):
        element = self.driver.find_element(*ProductsListPageLocators.LOAD_MORE_BUTTON)
        element.click()

    def get_price(self, product):
        element = product.find_element(*ProductsListPageLocators.ITEM_PRICE)
        return element

    def click_sale_button(self, product):
        element = product.find_element(*ProductsListPageLocators.SALE_BUTTON)
        element.click()

    def get_price_after_adding(self):
        element = self.driver.find_element(*ProductPageLocators.COST_FROM_MODAL)
        return element

class ContactsPage(BasePage):
    def get_claims_phone(self):
        element = self.driver.find_element(*ContactsPageLocators.CLAIMS_PHONE)
        return element
