from selenium.webdriver.common.by import By

TARIFF_WORKING = (
    By.XPATH, "//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title') and text()='Рабочий']]"
)
TARIFF_SLEEPY = (
    By.XPATH, "//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title') and text()='Сонный']]"
)
TARIFF_VACATION = (
    By.XPATH, "//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title') and text()='Отпускной']]"
)
TARIFF_TALKATIVE = (
    By.XPATH, "//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title') and text()='Разговорчивый']]"
)
TARIFF_CONSOLING = (
    By.XPATH, "//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title') and text()='Утешительный']]"
)
TARIFF_GLOSSY = (
    By.XPATH, "//div[contains(@class,'tcard')][.//div[contains(@class,'tcard-title') and text()='Глянцевый']]"
)

ALL_TARIFFS_TITLES = (By.CSS_SELECTOR, ".tariff-cards .tcard .tcard-title")
ACTIVE_TARIFF = (By.CSS_SELECTOR, ".tariff-cards .tcard.active")

TARIFF_INFO_BUTTON_INNER = (By.CSS_SELECTOR, ".i-button")
TARIFF_TOOLTIP_INNER = (By.CSS_SELECTOR, ".i-floating-tooltip")
TARIFF_TOOLTIP_DESCRIPTION_INNER = (By.CSS_SELECTOR, ".i-dPrefix")

TARIFF_LOCATORS = {
    "Рабочий": TARIFF_WORKING,
    "Сонный": TARIFF_SLEEPY,
    "Отпускной": TARIFF_VACATION,
    "Разговорчивый": TARIFF_TALKATIVE,
    "Утешительный": TARIFF_CONSOLING,
    "Глянцевый": TARIFF_GLOSSY,
}

PHONE_BUTTON = (By.CSS_SELECTOR, ".form .np-button")
PAYMENT_BUTTON = (By.CSS_SELECTOR, ".form .pp-button")

COMMENT_FIELD = (By.CSS_SELECTOR, ".form #comment")

REQUIREMENTS_BLOCK = (By.CSS_SELECTOR, ".form .reqs")

LAPTOP_TABLE_SLIDER = (By.CSS_SELECTOR, ".reqs .switch .slider")

SUBMIT_ORDER_BTN = (By.CSS_SELECTOR, ".smart-button-wrapper .smart-button")

ORDER_HEADER_TITLE = (By.CSS_SELECTOR, ".order-header-title")
ORDER_TIMER = (By.CSS_SELECTOR, ".order-header-time")


ORDER_CANCEL_BTN = (By.XPATH, "//div[contains(@class,'order-btn-group')][.//div[text()='Отменить']]//button")
ORDER_DETAILS_BTN = (By.XPATH, "//div[contains(@class,'order-btn-group')][.//div[text()='Детали']]//button")