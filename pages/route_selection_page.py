from locators import route_selection_page_locators
from pages.base_page import BasePage
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec

class RouteSelectionPage(BasePage):
    
    def route_selection_block(self):
        return self.wait_element_visible(
            route_selection_page_locators.ROUTE_SELECTION_BLOCK
        )

    def optimal_route_mode(self):
        return self.wait_element_visible(
            route_selection_page_locators.OPTIMAL_MODE
        )

    def fast_route_mode(self):
        return self.wait_element_visible(
            route_selection_page_locators.FAST_MODE
        )

    def custom_route_mode(self):
        return self.wait_element_visible(
            route_selection_page_locators.CUSTOM_MODE
        )

    def transport_car(self):
        return self.wait_element_visible(
            route_selection_page_locators.TRANSPORT_CAR
        )

    def transport_walk(self):
        return self.wait_element_visible(
            route_selection_page_locators.TRANSPORT_WALK
        )

    def transport_taxi(self):
        return self.wait_element_visible(
            route_selection_page_locators.TRANSPORT_TAXI
        )

    def transport_bike(self):
        return self.wait_element_visible(
            route_selection_page_locators.TRANSPORT_BIKE
        )

    def transport_scooter(self):
        return self.wait_element_visible(
            route_selection_page_locators.TRANSPORT_SCOOTER
        )

    def transport_drive(self):
        return self.wait_element_visible(
            route_selection_page_locators.TRANSPORT_DRIVE
        )

    def route_time_duration(self):
        return self.wait_element_visible(
            route_selection_page_locators.ROUTE_TIME_DURATION
        )

    def cost_of_trip(self):
        return self.wait_element_visible(
            route_selection_page_locators.COST_OF_TRIP
        )

    def call_taxi_btn(self):
        return self.wait_element_visible(
            route_selection_page_locators.CALL_TAXI_BTN
        )

    def to_book_btn(self, timeout=20):
        return self.wait_element_visible(
            route_selection_page_locators.BOOK_DRIVE_BTN,
            timeout
        )

    def transport_drive_btn_click(self):
        return self.click_to_element(
            route_selection_page_locators.TRANSPORT_DRIVE
        )

    def call_taxi_btn_click(self):
        self.click_to_element(
            route_selection_page_locators.CALL_TAXI_BTN
        )

    def custom_route_btn_click(self):
        self.click_to_element(
            route_selection_page_locators.CUSTOM_MODE
        )

    def optimal_route_btn_click(self):
        self.click_to_element(
            route_selection_page_locators.OPTIMAL_MODE
        )

    def fast_route_btn_click(self):
        self.click_to_element(
            route_selection_page_locators.FAST_MODE
        )

    def free_car_message(self):
        return self.wait_element_visible(
            route_selection_page_locators.FREE_CAR
        )

    def zero_route_time_duration(self):
        return self.wait_element_visible(
            route_selection_page_locators.ZERO_ROUTE_TIME_DURATION
        )

    def is_optimal_mode_active(self, timeout = None):
        try:
            self._wait(timeout).until(
                ec.visibility_of_element_located(
                    route_selection_page_locators.OPTIMAL_MODE_ACTIVE
                )
            )
            return True
        except TimeoutException:
            return False

    def is_fast_mode_active(self, timeout = None):
        try:
            self._wait(timeout).until(
                ec.visibility_of_element_located(
                    route_selection_page_locators.FAST_MODE_ACTIVE
                )
            )
            return True
        except TimeoutException:
            return False

    def is_custom_mode_active(self, timeout = None):
        try:
            self._wait(timeout).until(
                ec.visibility_of_element_located(
                    route_selection_page_locators.CUSTOM_MODE_ACTIVE
                )
            )
            return True
        except TimeoutException:
            return False

    def are_transport_types_enabled(self):
        locators = [
            route_selection_page_locators.TRANSPORT_CAR,
            route_selection_page_locators.TRANSPORT_WALK,
            route_selection_page_locators.TRANSPORT_TAXI,
            route_selection_page_locators.TRANSPORT_BIKE,
            route_selection_page_locators.TRANSPORT_SCOOTER,
            route_selection_page_locators.TRANSPORT_DRIVE,
        ]
        return all(
            "disabled" not in self.find_element(loc).get_attribute("class").split()
            for loc in locators
        )

    def is_call_taxi_btn_clickable(self):
        return self.wait_element_clickable(route_selection_page_locators.CALL_TAXI_BTN)

    def wait_to_book_btn_clickable(self, timeout=20):
        try:
            self._wait(timeout).until(
                ec.element_to_be_clickable(route_selection_page_locators.BOOK_DRIVE_BTN)
            )
            return True
        except TimeoutException:
            return False