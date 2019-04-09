import pytest
import logging

from helpers.utils import *
from helpers.page import *
from lib.fixtures import expected_data


logger = logging.getLogger('ui_site')
PATH = '/contacts/1.html'

class TestContacts:
    """Test contacts"""

    def setup_class(cls):
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    def test_claims(self, selenium, main_url):
        """claims phone"""

        selenium.get(main_url + PATH)
        contacts_page = ContactsPage(selenium)
        claims_phone = contacts_page.get_claims_phone().text

        assert(claims_phone == expected_data.CONTACTS['claims']['phone'])
