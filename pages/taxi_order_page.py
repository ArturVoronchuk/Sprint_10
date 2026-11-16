from selenium.common import TimeoutException

from locators import taxi_order_page_locators
from pages.base_page import BasePage

class TaxiOrderPage(BasePage):

    def tariff_titles(self):
        return [
            el.get_attribute("textContent").strip()
            for el in self.find_all(taxi_order_page_locators.ALL_TARIFFS_TITLES)
        ]

    def active_tariffs(self):
        return self.find_all(taxi_order_page_locators.ACTIVE_TARIFF)

    def select_tariff(self, tariff_name):
        self.click_to_element(taxi_order_page_locators.TARIFF_LOCATORS[tariff_name])

    def hover_tariff_info(self, tariff_name):
        tariff = self.find_element(taxi_order_page_locators.TARIFF_LOCATORS[tariff_name])
        self.hover(tariff)
        info_btn = tariff.find_element(*taxi_order_page_locators.TARIFF_INFO_BUTTON_INNER)
        self.hover(info_btn)

    def is_tariff_tooltip_shown(self, tariff_name):
        tariff = self.find_element(taxi_order_page_locators.TARIFF_LOCATORS[tariff_name])
        try:
            self._wait(3).until(
                lambda d: "show" in tariff.find_element(
                    *taxi_order_page_locators.TARIFF_TOOLTIP_INNER
                ).get_attribute("class")
            )
            return True
        except TimeoutException:
            return False

    def tariff_description(self, tariff_name):
        tariff = self.find_element(taxi_order_page_locators.TARIFF_LOCATORS[tariff_name])
        tooltip = tariff.find_element(*taxi_order_page_locators.TARIFF_TOOLTIP_INNER)
        return tooltip.find_element(
            *taxi_order_page_locators.TARIFF_TOOLTIP_DESCRIPTION_INNER
        ).text

    def phone_field(self):
        return self.wait_element_visible(taxi_order_page_locators.PHONE_BUTTON)

    def payment_field(self):
        return self.wait_element_visible(taxi_order_page_locators.PAYMENT_BUTTON)

    def comment_field(self):
        return self.wait_element_visible(taxi_order_page_locators.COMMENT_FIELD)

    def requirements_field(self):
        return self.wait_element_visible(taxi_order_page_locators.REQUIREMENTS_BLOCK)

    def order_requirements_btn_click(self):
        self.click_to_element(taxi_order_page_locators.REQUIREMENTS_BLOCK)

    def laptop_table_checkbox_click(self):
        self.click_to_element(taxi_order_page_locators.LAPTOP_TABLE_SLIDER)

    def fill_phone_and_order_btn_click(self):
        self.click_to_element(taxi_order_page_locators.SUBMIT_ORDER_BTN)

    def searching_car_header(self):
        return self.wait_element_visible(taxi_order_page_locators.ORDER_HEADER_TITLE)

    def countdown_timer(self):
        return self.wait_element_visible(taxi_order_page_locators.ORDER_TIMER)

    def searching_car_cancel_btn(self):
        return self.wait_element_visible(taxi_order_page_locators.ORDER_CANCEL_BTN)

    def searching_car_details_btn(self):
        return self.wait_element_visible(taxi_order_page_locators.ORDER_DETAILS_BTN)