import allure
import pytest

from data import EXPECTED_TARIFFS, TARIFF_DESCRIPTIONS


@allure.feature("Проверяем функционал выбора тарифа такси")
class TestTaxiFares:

    @allure.title(
        "Проверяем, что в открывшейся форме заказа такси есть все шесть тарифов"
        "и что один из тарифов в статусе active"
    )
    def test_taxi_order_form_shows_6_tariffs_with_one_active(
            self, taxi_order_page
    ):
        with allure.step("Проверяем, что отображаются все 6 тарифов по ТЗ (в порядке ТЗ)"):
            assert taxi_order_page.tariff_titles() == EXPECTED_TARIFFS, \
                f"Тарифы не совпадают с ТЗ: {taxi_order_page.tariff_titles()}"

        with allure.step("Проверяем, что активен ровно один тариф"):
            active = taxi_order_page.active_tariffs()
            assert len(active) == 1, \
                f"Активных тарифов должно быть 1, а не {len(active)}"

    @allure.title(
        "При наведении на иконку i в правом верхнем углу каждого тарифа отображается "
        "всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ"
    )
    @pytest.mark.parametrize("tariff_name", [
        "Рабочий",
        pytest.param(
            "Сонный",
            marks=pytest.mark.xfail(
                reason="Баг AAA-001: фактическое описание тарифа 'Сонный' — "
                       "'Если мысли не выходят из головы', "
                        "а по ТЗ должно быть описание — 'Для тех, кто не выспался'"
            ),
        ),
        "Отпускной",
        pytest.param(
            "Разговорчивый",
            marks=pytest.mark.xfail(
                reason="Баг ААА-002 фактическое описание тарифа 'Разговорчивый' — "
                       "'Для тех, кто не выспался', "
                        "а по ТЗ должно быть описание — 'Если мысли не выходят из головы'"
            ),
        ),
        "Утешительный",
        "Глянцевый",
    ])
    def test_tariff_description_on_hover(
            self, taxi_order_page, tariff_name
    ):
        with allure.step(f"Выбираем тариф '{tariff_name}'"):
            taxi_order_page.select_tariff(tariff_name)

        with allure.step(f"Наводим на 'i' тарифа '{tariff_name}'"):
            taxi_order_page.hover_tariff_info(tariff_name)

        with allure.step("Проверяем, что тултип отображается"):
            assert taxi_order_page.is_tariff_tooltip_shown(tariff_name), \
                "Тултип не отображается"

        with allure.step("Проверяем описание тарифа в тултипе"):
            assert taxi_order_page.tariff_description(tariff_name) == TARIFF_DESCRIPTIONS[tariff_name], \
                "Описание тарифа в тултипе отсутствует"

    @allure.title(
        "Проверяем, что под каждым тарифом отображется блок с полями: "
        "Телефон, Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси "
    )
    @pytest.mark.parametrize("tariff_name", [
        "Рабочий",
        "Сонный",
        "Отпускной",
        "Разговорчивый",
        "Утешительный",
        "Глянцевый",
    ])
    def test_fares_displays_block_with_fields(
            self, taxi_order_page, tariff_name
    ):
        with allure.step(f"Выбираем тариф '{tariff_name}'"):
            taxi_order_page.select_tariff(tariff_name)

        with allure.step(
                "Проверяем, что отображается поле 'Телефон' в блоке настройки заказа такси"
        ):
            assert taxi_order_page.phone_field().is_displayed(), \
                "Поле 'Телефон' не отображается"

        with allure.step(
                "Проверяем, что отображается поле 'Способ оплаты' в блоке настройки заказа такси"
        ):
            assert taxi_order_page.payment_field().is_displayed(), \
                "Поле 'Способ оплаты' не отображается"

        with allure.step(
                "Проверяем, что отображается поле 'Комментарий водителю' в блоке настройки заказа такси"
        ):
            assert taxi_order_page.comment_field().is_displayed(), \
                "Поле 'Комментарий водителю' не отображается"

        with allure.step(
                "Проверяем, что отображается блок 'Требования к заказу' в блоке настройки заказа такси"
        ):
            assert taxi_order_page.requirements_field().is_displayed(), \
                "Блок 'Требования к заказу' не отображается"