from selenium.common import TimeoutException

from locators import taxi_completed_order_page_locators as locators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec

class TaxiCompletedOrderPage(BasePage):

    def wait_completed_order(self, timeout=40):
        return self.wait_element_visible(locators.DRIVER_RATING, timeout)

    def header(self):
        return self.wait_element_visible(locators.COMPLETED_HEADER)

    def car_number(self):
        return self.wait_element_visible(locators.CAR_NUMBER)

    def car_tariff_image(self):
        return self.wait_element_visible(locators.CAR_TARIFF_IMAGE)

    def driver_rating(self):
        return self.wait_element_visible(locators.DRIVER_RATING)

    def driver_name(self):
        return self.wait_element_visible(locators.DRIVER_NAME)

    def driver_photo(self):
        return self.wait_element_visible(locators.DRIVER_PHOTO)

    def cancel_btn(self):
        return self.wait_element_visible(locators.CANCEL_BTN)

    def details_btn(self):
        return self.wait_element_visible(locators.DETAILS_BTN)

    def click_details(self):
        self.click_to_element(locators.DETAILS_BTN)

    def click_cancel(self):
        self.click_to_element(locators.CANCEL_BTN)

    def details_block(self):
        return self.wait_element_visible(locators.DETAILS_SHOWN)

    def pickup_address(self):
        return self.wait_element_visible(locators.PICKUP_ADDRESS)

    def destination_address(self):
        return self.wait_element_visible(locators.DESTINATION_ADDRESS)

    def payment_method(self):
        return self.wait_element_visible(locators.PAYMENT_METHOD)

    def trip_cost(self):
        return self.wait_element_visible(locators.TRIP_COST)

    def is_order_window_closed(self, timeout=10):
        try:
            self._wait(timeout).until(
                ec.invisibility_of_element_located(locators.COMPLETED_HEADER)
            )
            return True
        except TimeoutException:
            return False