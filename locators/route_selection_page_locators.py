from selenium.webdriver.common.by import By

ROUTE_SELECTION_BLOCK = (By.CSS_SELECTOR, ".modes-container")

OPTIMAL_MODE = (By.XPATH, "//div[contains(@class,'mode') and text()='Оптимальный']")
FAST_MODE = (By.XPATH, "//div[contains(@class,'mode') and text()='Быстрый']")
CUSTOM_MODE = (By.XPATH, "//div[contains(@class,'mode') and text()='Свой']")

COST_OF_TRIP = (
    By.XPATH,
    "//div[contains(@class,'results-text')]//div[contains(@class,'text')]"
)
ROUTE_TIME_DURATION = (
    By.XPATH,
    "//div[contains(@class,'results-text')]//div[contains(@class,'duration')]"
)

CALL_TAXI_BTN = (By.XPATH, "//div[contains(@class,'results-text')]//button[text()='Вызвать такси']")
BOOK_DRIVE_BTN = (By.XPATH, "//div[contains(@class,'results-text')]//button[text()='Забронировать']")

TRANSPORT_CAR = (By.CSS_SELECTOR, ".types-container .type:has(img[src*='car'])")
TRANSPORT_WALK = (By.CSS_SELECTOR, ".types-container .type:has(img[src*='walk'])")
TRANSPORT_TAXI = (By.CSS_SELECTOR, ".types-container .type:has(img[src*='taxi'])")
TRANSPORT_BIKE = (By.CSS_SELECTOR, ".types-container .type:has(img[src*='bike'])")
TRANSPORT_SCOOTER = (By.CSS_SELECTOR, ".types-container .type:has(img[src*='scooter'])")
TRANSPORT_DRIVE = (By.CSS_SELECTOR, ".types-container .type:has(img[src*='drive'])")

FREE_CAR = (
    By.XPATH,
    "//div[contains(@class,'results-text')]//div[contains(@class,'text') and text()='Авто Бесплатно']"
)
ZERO_ROUTE_TIME_DURATION = (
    By.XPATH,
    "//div[contains(@class,'results-text')]//div[contains(@class,'duration') and text()='В пути 0 мин.']"
)

FAST_MODE_ACTIVE = (
    By.XPATH,
    "//div[contains(@class,'mode') and contains(@class,'active') and text()='Быстрый']"
)

OPTIMAL_MODE_ACTIVE = (
    By.XPATH,
    "//div[contains(@class,'mode') and contains(@class,'active') and text()='Оптимальный']"
)

CUSTOM_MODE_ACTIVE = (
    By.XPATH,
    "//div[contains(@class,'mode') and contains(@class,'active') and text()='Свой']"
)
