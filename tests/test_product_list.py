import pytest
import logging

from helpers.utils import *
from helpers.page import *


logger = logging.getLogger('ui_site')
PATH = '/instrument/'

class TestAddProductFromList:
    """Test add product from list"""

    def setup_class(cls):
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    def test_with_bonuses(self, selenium, main_url):
        """with_bonuses"""

        selenium.get(main_url + PATH)
        products_list_page = ProductsListPage(selenium)
        product = products_list_page.get_product_with_bonuses()

        while not product:
            products_list_page.click_load_more()
            product = products_list_page.get_product_with_bonuses()

        selenium.execute_script("arguments[0].scrollIntoView();", product)

        saled_price = get_int(products_list_page.get_price(product).text)
        products_list_page.click_sale_button(product)

        price_after_adding = get_int(products_list_page.get_price_after_adding().text)

        assert(saled_price == price_after_adding)
