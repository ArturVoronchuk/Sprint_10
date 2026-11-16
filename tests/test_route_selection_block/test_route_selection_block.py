import allure

from data import free_car_msg, zero_route_time_msg

@allure.feature("Проверяем отображение функционала блока выбора маршрута")
class TestDrawingRoute:

    @allure.title(
        "Проверяем, что при вводе двух разных предустановленных адресов "
        "в поля 'Откуда' и 'Куда' под выбором адресов в блоке "
        "выбора маршрута отображаются виды маршрута: "
        "Оптимальный, Быстрый, Свой"
    )
    def test_route_modes_displayed(
            self, route_page_two_addr
    ):

        with allure.step("Проверяем, что блок выбора маршрута отображается"):
            assert route_page_two_addr.route_selection_block().is_displayed(), \
                "Блок выбора маршрута не отображается"

        with allure.step(
                "Проверяем, что в блоке выбора маршрута отображается "
                "режим 'Оптимальный'"
        ):
            assert route_page_two_addr.optimal_route_mode().is_displayed(), \
                "В блоке выбора маршрута не отображается режим 'Оптимальный'"

        with allure.step(
                "Проверяем, что в блоке выбора маршрута отображается "
                "режим 'Быстрый'"
        ):
            assert route_page_two_addr.fast_route_mode().is_displayed(), \
                "В блоке выбора маршрута НЕ отображается режим 'Быстрый'"

        with allure.step(
                "Проверяем, что в блоке выбора маршрута отображается "
                "режим 'Свой'"
        ):
            assert route_page_two_addr.custom_route_mode().is_displayed(), \
                "в блоке выбора маршрута не отображается режим 'Свой'"

    @allure.title(
        "Проверяем, что при вводе двух разных предустановленных адресов "
        "в поля 'Откуда' и 'Куда' под выбором адресов в блоке "
        "выбора маршрута отображаются типы передвижения: "
        "Машина, Пешком, Такси, Велосипед, Самокат, Двайв; "
    )
    def test_transport_types_displayed(
            self, route_page_two_addr
        ):

        with allure.step(
                "Проверяем, что тип передвижения 'Машина' отображается"
        ):
            assert route_page_two_addr.transport_car().is_displayed(), \
                "Тип передвижения 'Машина' не отображается"

        with allure.step(
                "Проверяем, что тип передвижения 'Пешком' отображается"
        ):
            assert route_page_two_addr.transport_walk().is_displayed(), \
                "Тип передвижения 'Пешком' не отображается"

        with allure.step(
                "Проверяем, что тип передвижения 'Такси' отображается"
        ):
            assert route_page_two_addr.transport_taxi().is_displayed(), \
                "Тип передвижения 'Такси' не отображается"

        with allure.step(
                "Проверяем, что тип передвижения 'Велосипед' отображается"
        ):
            assert route_page_two_addr.transport_bike().is_displayed(), \
                "Тип передвижения 'Велосипед' не отображается"

        with allure.step(
                "Проверяем, что тип передвижения 'Самокат' отображается"
        ):
            assert route_page_two_addr.transport_scooter().is_displayed(), \
                "Тип передвижения 'Самокат' не отображается"

        with allure.step(
                "Проверяем, что тип передвижения 'Драйв' отображается"
        ):
            assert route_page_two_addr.transport_drive().is_displayed(), \
                "Тип передвижения 'Драйв' не отображается"

    @allure.title(
        "Проверяем, что при вводе двух разных предустановленных адресов "
        "в поля 'Откуда' и 'Куда' под выбором адресов в блоке "
        "выбора маршрута отображается блок информации: "
        "Стоимость, Время в пути; "
    )
    def test_block_with_route_time_duration_and_route_cost_is_displayed(
            self, route_page_two_addr
        ):

        with allure.step(
                "Проверяем, что отображается стоимость поездки"
        ):
            price = route_page_two_addr.cost_of_trip()
            assert price.is_displayed()
            assert price.text.strip() != "", \
                "Стоимость поездки не отображается (пустой текст)"

        with allure.step(
                "Проверяем, что отображается время поездки"
        ):
            duration = route_page_two_addr.route_time_duration()
            assert duration.is_displayed()
            assert duration.text.strip() != "", \
                "Время поездки не отображается (пустой текст)"

    @allure.title(
        "Проверяем, что при вводе двух разных предустановленных адресов "
        "в поля 'Откуда' и 'Куда' под выбором адресов в блоке "
        "выбора маршрута отображаются: "
        "кнопка 'Вызвать' такси для типа Такси; "
    )
    def test_call_taxi_btn_displayed(
            self, route_page_two_addr
    ):

        with allure.step(
                "Проверяем, что отображается кнопка вызова такси для типа передвижения 'Такси'"
        ):
            assert route_page_two_addr.call_taxi_btn().is_displayed(), \
                "Кнопка вызова такси для типа передвижения 'Такси' не отображжается"

    @allure.title(
        "Проверяем, что при вводе двух разных предустановленных адресов "
        "в поля 'Откуда' и 'Куда' под выбором адресов в блоке "
        "выбора маршрута в режиме маршрута 'Свой' отображается "
        "кнопка 'Забронировать' для типа 'Двайв'"
    )
    def test_for_drive_type_booking_btn_is_displayed(
            self, route_page_two_addr
    ):

        with allure.step("Кликаем по типу маршрута 'Свой'"):
            route_page_two_addr.custom_route_btn_click()

        with allure.step("Кликаем по типу передвижения 'Драйв'"):
            route_page_two_addr.transport_drive_btn_click()

        with allure.step("Проверяем, что кнопка 'Забронировать' отображается"):
            assert route_page_two_addr.to_book_btn().is_displayed(), \
                "Кнопка 'Забронировать' не отображается"

    @allure.title(
        "Проверяем, что при вводе двух одинаковых предустановленных адресов "
        "в поля 'Откуда' и 'Куда' под выбором адресов  отображается блок с выбором "
        "маршрута с текстом 'Авто Бесплатно В пути 0 мин.' "
    )
    def test_same_address_shows_auto_free_message(
            self, route_page_same_addr
    ):

        with allure.step(
                "Проверяем, что в блоке с выбором маршрута отображается сообщщение "
                "'Авто Бесплатно'"
        ):
            assert route_page_same_addr.free_car_message().text == free_car_msg, \
                "В блоке с выбором маршрута нет сообщщения 'Авто Бесплатно'"

        with allure.step(
                "Проверяем, что в блоке с выбором маршрута отображается сообщщение "
                "'В пути 0 мин.'"
        ):
            assert route_page_same_addr.zero_route_time_duration().text == zero_route_time_msg, \
                "В блоке с выбором маршрута нет сообщщения 'В пути 0 мин.'"
