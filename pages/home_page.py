from locators import home_page_locators
from pages.base_page import BasePage

class HomePage(BasePage):

    def enter_route_point_where_from(self, text):
        self.send_keys(
            home_page_locators.WHERE_FROM_FIELD,
            text
        )

    def enter_route_point_where_to(self, text):
        self.send_keys(
            home_page_locators.WHERE_TO_FIELD,
            text
        )

    def route_points(self):
        return self.find_all(
            home_page_locators.ROUTE_POINTS
        )

    def route_point_addresses(self):
        return [
            el.text for el in self.find_all(
                home_page_locators.ROUTE_POINT_TEXT
            )
        ]
