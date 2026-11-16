from selenium.webdriver.common.by import By

COMPLETED_HEADER = (By.CSS_SELECTOR, ".order-header-title")

CAR_NUMBER = (By.CSS_SELECTOR, ".order-number .number")
CAR_TARIFF_IMAGE = (By.CSS_SELECTOR, ".order-number img")

DRIVER_RATING = (By.CSS_SELECTOR, ".order-btn-rating")
DRIVER_NAME = (By.XPATH, "//div[contains(@class,'order-btn-group')][.//div[contains(@class,'order-btn-rating')]]/div[last()]")
DRIVER_PHOTO = (By.XPATH, "//div[contains(@class,'order-btn-group')][.//div[contains(@class,'order-btn-rating')]]//img")

CANCEL_BTN = (By.XPATH, "//div[contains(@class,'order-btn-group')][.//div[text()='Отменить']]//button")
DETAILS_BTN = (By.XPATH, "//div[contains(@class,'order-btn-group')][.//div[text()='Детали']]//button")

DETAILS_SHOWN = (By.CSS_SELECTOR, ".order-details.shown")
PICKUP_ADDRESS = (By.XPATH, "//div[contains(@class,'o-d-sh') and text()='Адрес подачи']/preceding-sibling::div[contains(@class,'o-d-h')]")
DESTINATION_ADDRESS = (By.XPATH, "//div[contains(@class,'o-d-sh') and text()='Адрес назначения']/preceding-sibling::div[contains(@class,'o-d-h')]")
PAYMENT_METHOD = (By.XPATH, "//div[contains(@class,'o-d-sh') and text()='Способ оплаты']/preceding-sibling::div[contains(@class,'o-d-h')]")
TRIP_COST = (By.XPATH, "//div[contains(@class,'o-d-sh') and starts-with(., 'Стоимость')]")
