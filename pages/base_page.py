from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:

    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.timeout = timeout

    def _wait(self, timeout = None):
        if timeout is None:
            timeout = self.timeout
        return WebDriverWait(self.driver, timeout)

    def send_keys(self, locator, text):
        element = self._wait().until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        return self._wait(timeout).until(ec.presence_of_element_located(locator))

    def find_all(self, locator, timeout=None):
        return self._wait(timeout).until(
            ec.presence_of_all_elements_located(locator)
        )

    def wait_element_visible(self, locator, timeout=None):
        return self._wait(timeout).until(
            ec.visibility_of_element_located(locator)
        )

    def click_to_element(self, locator, timeout=None):
        self._wait(timeout).until(ec.element_to_be_clickable(locator)).click()

    def wait_element_clickable(self, locator, timeout=None):
        try:
            self._wait(timeout).until(ec.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def hover(self, element):
        ActionChains(self.driver).move_to_element(element).perform()