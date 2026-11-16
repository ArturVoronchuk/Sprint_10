import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import first_preset_route, second_preset_route
from pages.home_page import HomePage
from pages.route_selection_page import RouteSelectionPage
from pages.taxi_completed_order_page import TaxiCompletedOrderPage
from pages.taxi_order_page import TaxiOrderPage
from urls import MAIN_PAGE

@pytest.fixture(scope="function")
def driver():
    options = Options()
    #options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def home_page(driver):
    page = HomePage(driver)
    page.go_to_url(MAIN_PAGE)
    return page

@pytest.fixture
def route_page_two_addr(driver, home_page):
    with allure.step("Вводим адрес в поле 'Откуда'"):
        home_page.enter_route_point_where_from(first_preset_route)
    with allure.step("Вводим адрес в поле 'Куда'"):
        home_page.enter_route_point_where_to(second_preset_route)
    return RouteSelectionPage(driver)

@pytest.fixture
def route_page_same_addr(driver, home_page):
    with allure.step(f"Вводим адрес {first_preset_route} в 'Откуда'"):
        home_page.enter_route_point_where_from(first_preset_route)
    with allure.step(f"Вводим адрес {first_preset_route} в 'Куда'"):
        home_page.enter_route_point_where_to(first_preset_route)
    return RouteSelectionPage(driver)

@pytest.fixture
def taxi_order_page(driver, route_page_two_addr):
    with allure.step("Кликаем на кнопку 'Вызвать такси'"):
        route_page_two_addr.call_taxi_btn_click()
    return TaxiOrderPage(driver)

@pytest.fixture
def taxi_completed_order_page(driver, taxi_order_page):
    with allure.step("Раскрываем 'Требования к заказу'"):
        taxi_order_page.order_requirements_btn_click()
    with allure.step("Включаем чекбокс 'Столик для ноутбука'"):
        taxi_order_page.laptop_table_checkbox_click()
    with allure.step("Нажимаем 'Ввести номер и заказать'"):
        taxi_order_page.fill_phone_and_order_btn_click()

    page = TaxiCompletedOrderPage(driver)
    with allure.step("Ждём окно совершённого заказа (после таймера)"):
        page.wait_completed_order()
    return page