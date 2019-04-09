from selenium.webdriver.common.by import By

from helpers.utils import translator


class BasePageLocators(object):
    REGION_LINK = (By.XPATH, '//*[contains(@class, "iconRegion")]/following-sibling::span')
    CITY_LINK = (By.XPATH, '//*[contains(@class, "region_check")]')
    CITY_WITH_DELIVERY_LINK = (By.XPATH, '//*[contains(@class, "region_check") and not(contains(@class, "fst-b"))]')

class ProductPageLocators(object):
    ADD_BY_SALE_BUTTON = (By.XPATH, '//div[@class="retail-sale__buttons"]/a')

    SALED_PRICE = (By.XPATH,
            '//div[@class="retail-sale__body"]/span[@class="price-value"]')
    COST_FROM_MODAL = (By.ID, 'cartAllCost')

class ProductsListPageLocators(object):
    PRODUCT_WITH_BONUSES = (By.XPATH, f'//div[@class="tile-box product"][descendant::span[contains(@class, "color-blue") and contains(text(), "{translator.get_translation("vi.product.labels.high_bonus")}")]]')
    LOAD_MORE_BUTTON = (By.XPATH, '//span[@class="showMore"]')
    ITEM_PRICE = (By.XPATH, '//div[@class="price-actual -no-old"]')
    SALE_BUTTON = (By.XPATH, '//div[@class="buttons"]')
    COST_FROM_MODAL = (By.ID, 'cartAllCost')


class ContactsPageLocators(object):
    CLAIMS_PHONE = (By.XPATH, f'//td[contains(text(), "{translator.get_translation("vi.contacts.claims_dep")}")]/following-sibling::td[@class="contact_info_table_telefon"]')
