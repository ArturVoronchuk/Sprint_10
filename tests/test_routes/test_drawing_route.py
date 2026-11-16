import allure

from data import first_preset_route, second_preset_route
from helpers.helpers import normalize_address


@allure.feature("Проверяем функционал отрисовки маршрута")
class TestDrawingRoute:

    @allure.title(
        "Проверяем, что при вводе двух разных предустановленных адресов "
        "в поля 'Откуда' и 'Куда' на карте отображаются две точки "
        "начала и конца маршрута"
    )
    def test_entering_address_appear_start_and_end_points_of_route(
            self, home_page
    ):
        with allure.step("Вводим адрес в поле 'Откуда'"):
            home_page.enter_route_point_where_from(first_preset_route)

        with allure.step("Вводим адрес в поле 'Куда'"):
            home_page.enter_route_point_where_to(second_preset_route)

        with allure.step("Проверяем, что на карте две точки маршрута"):
            points = home_page.route_points()
            assert len(points) == 2, \
                f"Количество точек на карте {len(points)}, а должно быть 2"

        with allure.step("Проверяем, что адреса точек соответствуют введённым"):
            addresses = [normalize_address(a) for a in home_page.route_point_addresses()]
            assert first_preset_route in addresses
            assert second_preset_route in addresses, \
                "Адреса точек не соответствуют введенным адресам"
