import pytest
import logging

from helpers.utils import *
from helpers.page import *


logger = logging.getLogger('ui_site')
PATH = '/stanki/kombinirovannye-po-derevu/visprom/cwm-200-3-220-35220000/'

class TestAddProductToBucket:
    """Test add to bucket"""

    def setup_class(cls):
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    def test_sale_price(self, selenium, main_url):
        """by sale price"""

        selenium.get(main_url + PATH)
        product_page = ProductPage(selenium)
        saled_price = get_int(product_page.get_saled_price().text)
        product_page.click_sale_button()

        price_after_adding = get_int(product_page.get_price_after_adding().text)

        assert(saled_price == price_after_adding)
