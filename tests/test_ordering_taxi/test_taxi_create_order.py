import re

import allure
from data import searching_car


@allure.feature("Проверяем функциона создания заказа такси")
class TestTaxiCreateOrder:

    @allure.title(
        "Проверяем, что в тарифе 'Рабочий' при нажатии на кнопку 'Ввести номер и заказать' "
        "появляется окно ожидания машины, содержащее: "
        "1) Заголовок: Поиск машины; "
        "2) Таймер обратного отсчета в правом верхнем углу; "
        "3) Кнопки: Отменить, Детали "
    )
    def test_taxi_waiting_window_appears_after_order(
            self, taxi_order_page
    ):
        with allure.step("Кликаем по кнопке 'Требования к заказу'"):
            taxi_order_page.order_requirements_btn_click()

        with allure.step("Кликаем по чекбоксу 'Столик для ноутбука'"):
            taxi_order_page.laptop_table_checkbox_click()

        with allure.step("Кликаем на кнопку 'Ввести номер и заказать'"):
            taxi_order_page.fill_phone_and_order_btn_click()

        with allure.step("Проверяем, что появился заголовок 'Поиск машины'"):
            header = taxi_order_page.searching_car_header()
            assert header.text == searching_car, \
            "Заголовок 'Поиск машины' не отображается в окне ожидания машины"

        with allure.step("Проверяем, что таймер обратного отсчета отображается"):
            assert taxi_order_page.countdown_timer().is_displayed(), \
            "Таймер обратного отсчета не отображается в окне ожидания машины"

        with allure.step("Проверяем, что таймер отображается в формате MM:SS"):
            assert re.fullmatch(r"\d{2}:\d{2}", taxi_order_page.countdown_timer().text), \
            "Формат таймера не соответствует MM:SS"

        with allure.step("Проверяем, что кнопка 'Отменить' отображается"):
            assert taxi_order_page.searching_car_cancel_btn().is_displayed(), \
            "Кнопка 'Отменить' не отображается в окне ожидания машины"

        with allure.step("Проверяем, что кнопка 'Детали' отображается"):
            assert taxi_order_page.searching_car_details_btn().is_displayed(), \
            "Кнопка 'Детали' не отображается в окне ожидания машины"