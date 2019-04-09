from selenium.webdriver.support.ui import WebDriverWait


class MainPageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver:
                driver.find_element(*self.locator))

        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

class ResultPageElement(object):
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver:
                driver.find_element(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute('value')
