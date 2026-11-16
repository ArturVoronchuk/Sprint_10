import allure

@allure.feature("Проверяем окно совершённого заказа такси")
class TestTaxiCompletedOrder:

    @allure.title(
        "После окончания таймера отображается окно совершённого заказа: "
        "заголовок 'n мин. и приедет', номер авто и картинка тарифа, "
        "водитель (имя, фото, рейтинг), кнопки 'Отменить' и 'Детали'"
    )
    def test_completed_order_elements_displayed(
            self, taxi_completed_order_page
    ):
        with allure.step("Заголовок 'n мин. и приедет'"):
            header_text = taxi_completed_order_page.header().text
            assert "мин" in header_text and "приедет" in header_text, \
                f"Заголовок не соответствует: {header_text}"

        with allure.step("Номер автомобиля отображается и не пустой"):
            number = taxi_completed_order_page.car_number()
            assert number.is_displayed()
            assert number.text.strip() != "", \
                "Номер авто пустой"

        with allure.step("Картинка тарифа отображается"):
            assert taxi_completed_order_page.car_tariff_image().is_displayed()

        with allure.step("Имя водителя отображается и не пустое"):
            name = taxi_completed_order_page.driver_name()
            assert name.is_displayed()
            assert name.text.strip() != "", \
                "Имя водителя пустое"

        with allure.step("Фото водителя отображается"):
            assert taxi_completed_order_page.driver_photo().is_displayed(), \
                "Фото водителя не отображается"

        with allure.step("Рейтинг водителя отображается"):
            assert taxi_completed_order_page.driver_rating().is_displayed(), \
                "Рейтинг водителя не отображается"

        with allure.step("Кнопка 'Отменить' отображается"):
            assert taxi_completed_order_page.cancel_btn().is_displayed(), \
                "Кнопка 'Отменить' отображается в окне завершенного заказа"

        with allure.step("Кнопка 'Детали' отображается"):
            assert taxi_completed_order_page.details_btn().is_displayed(), \
                "Кнопка 'Детали' отображается в окне завершенного заказа"

    @allure.title(
        "В окне совершённого заказа при нажатии 'Детали' указаны адрес подачи, "
        "адрес назначения, способ оплаты и стоимость"
    )
    def test_completed_order_details_displayed(
            self, taxi_completed_order_page
    ):
        with allure.step("Нажимаем 'Детали'"):
            taxi_completed_order_page.click_details()

        with allure.step("Блок деталей отображается"):
            assert taxi_completed_order_page.details_block().is_displayed(), \
                "Блок деталей не открылся"

        with allure.step("Адрес подачи отображается и не пустой"):
            pickup = taxi_completed_order_page.pickup_address()
            assert pickup.is_displayed()
            assert pickup.text.strip() != "", \
                "Адрес подачи не отображается или пустой"

        with allure.step("Адрес назначения отображается и не пустой"):
            destination = taxi_completed_order_page.destination_address()
            assert destination.is_displayed()
            assert destination.text.strip() != "", \
                "Адрес назначения не отображается или пустой"

        with allure.step("Способ оплаты отображается и не пустой"):
            payment = taxi_completed_order_page.payment_method()
            assert payment.is_displayed()
            assert payment.text.strip() != "", \
                "Способ оплаты не отображается или пустой"

        with allure.step("Стоимость отображается"):
            assert taxi_completed_order_page.trip_cost().is_displayed(), \
            "Стоимость поездки не отображается"

    @allure.title("При нажатии 'Отменить' окно совершённого заказа закрывается")
    def test_cancel_closes_order_window(self, taxi_completed_order_page):
        with allure.step("Нажимаем 'Отменить'"):
            taxi_completed_order_page.click_cancel()

        with allure.step("Окно совершённого заказа закрывается"):
            assert taxi_completed_order_page.is_order_window_closed(), \
                "Окно совершённого заказа не закрылось"