import pytest
import logging

from helpers.utils import *
from helpers.page import *
from lib.fixtures import expected_data


logger = logging.getLogger('ui_site')

class TestTitle:
    """Test title"""

    def setup_class(cls):
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    def test_ok(self, selenium, main_url):
        """on main page"""

        selenium.get(main_url)
        main_page = MainPage(selenium)

        assert(selenium.title == expected_data.TITLE)
