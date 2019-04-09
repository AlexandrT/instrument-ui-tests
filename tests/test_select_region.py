import pytest
import logging
import random

from helpers.utils import *
from helpers.page import *
from helpers.assertions import *
from lib.fixtures import expected_data


logger = logging.getLogger('ui_site')

class TestRegion:
    """Test region"""

    def setup_class(cls):
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    def test_open(self, selenium, main_url):
        """open"""

        selenium.get(main_url)
        main_page = MainPage(selenium)
        main_page.click_region()

        cities = []
        [ cities.append(item.text) for item in main_page.get_cities_links() ]

        assert_lists_equal(cities, expected_data.REGIONS)

    def test_select_with_delivery(self, selenium, main_url):
        """select with delivery"""

        selenium.get(main_url)
        main_page = MainPage(selenium)
        main_page.click_region()

        cities = main_page.get_cities_with_delivery_links()
        element = random.choice(cities)
        expected_city = element.text
        element.click()

        actual_city = main_page.get_region_link().text

        assert(expected_city == actual_city)
