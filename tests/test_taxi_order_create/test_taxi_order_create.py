import allure

from helpers.helpers import extract_number

@allure.feature("Проверяем отображение функционала блока выбора маршрута")
class TestTaxiOrderCreate:

    @allure.title(
        "Проверяем, что при переключении между видами маршрута (Оптимальный/Быстрый) "
        "происходит смена активного таба и пересчет времени и стоимости маршрута"
    )
    def test_switching_route_types_changes_active_tab_and_recalculates_route(
            self, route_page_two_addr
    ):

        with allure.step("Проверяем, что активен вида маршрута 'Быстрый'"):
            assert route_page_two_addr.is_fast_mode_active(), \
                "Вид маршрута 'Быстрый' не активен"

        with allure.step("Сохраняем значение цену и время поездки вида маршрута 'Быстрый'"):
            fast_mode_price = extract_number(route_page_two_addr.cost_of_trip().text)
            fast_mode_time = extract_number(route_page_two_addr.route_time_duration().text)

        with allure.step("Переключаемся на вид маршрута 'Оптимальный'"):
            route_page_two_addr.optimal_route_btn_click()

        with allure.step("Проверяем, что вид маршрута 'Оптимальный' стал активным"):
            assert route_page_two_addr.is_optimal_mode_active(), \
                "Вид маршрута 'Оптимальный' не стал активным"

        with allure.step("Проверяем, что стоимость поездки изменилась"):
            optimal_mode_price = extract_number(route_page_two_addr.cost_of_trip().text)
            assert fast_mode_price != optimal_mode_price, \
                "Стоимость поездки не изменилась"

        with allure.step("Проверяем, что время в пути изменилось"):
            optimal_mode_time = extract_number(route_page_two_addr.route_time_duration().text)
            assert fast_mode_time != optimal_mode_time, \
                "Время в пути не изменилось"

    @allure.title(
        "Проверяем, что при переключении на вид маршрута Свой происходит смена активного таба "
        "и становятся активны типы передвижения "
        "(Машина, Пешком, Такси, Велосипед, Самокат, Драйв)"
    )
    def test_switching_to_custom_type_changes_the_active(
            self, route_page_two_addr
    ):

        with allure.step("Кликаем на вид маршрута 'Свой'"):
             route_page_two_addr.custom_route_btn_click()

        with allure.step("Проверяем, что вид маршрута 'Свой' стал активным"):
            assert route_page_two_addr.is_custom_mode_active(), \
                "Вид маршрута 'Свой' не стал активным"

        with allure.step("Проверяем, что типы передвижения стали доступны (не disabled в DOM)"):
            assert route_page_two_addr.are_transport_types_enabled(), \
                "Типы передвижения остались disabled"

    @allure.title(
        "Проверяем, что при выборе вида маршрута 'Быстрый' активна кнопка 'Вызвать такси'"
    )
    def test_call_taxi_btn_is_clickable_in_fast_mode(
            self, route_page_two_addr
    ):

        with allure.step("Кликаем на вид маршрута 'Свой'"):
            route_page_two_addr.custom_route_btn_click()

        with allure.step("Кликаем на вид маршрута 'Быстрый'"):
            route_page_two_addr.fast_route_btn_click()

        with allure.step(
                "Проверяем, что тип передвижения 'Такси' стал активным (кликабельным)"
        ):
            assert route_page_two_addr.is_call_taxi_btn_clickable(), \
                "Тип передвижения 'Такси' не стал active"

    @allure.title(
        "Проверяем, что при выборе вида маршрута 'Свой', "
        "типа передвижения 'Драйв' активна кнопка 'Забронировать'"
    )
    def test_to_book_btn_is_clickable_in_custom_mode(
            self, route_page_two_addr
    ):
        with allure.step("Кликаем на вид маршрута 'Свой'"):
            route_page_two_addr.custom_route_btn_click()

        with allure.step("Кликаем на тип передвижения 'Драйв'"):
            route_page_two_addr.transport_drive_btn_click()

        with allure.step("Проверяем, что кнопка 'Забронировать' кликабельна"):
            assert route_page_two_addr.wait_to_book_btn_clickable(), \
                "Кнопка 'Забронировать' не кликабельна"