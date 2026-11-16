from selenium.webdriver.common.by import By

WHERE_FROM_FIELD = (By.XPATH, "//input[@id='from']")
WHERE_TO_FIELD = (By.XPATH, "//input[@id='to']")

ROUTE_POINTS = (By.CSS_SELECTOR, "ymaps[class*='placemark-overlay']")
ROUTE_POINT_TEXT = (By.CSS_SELECTOR, "ymaps[class*='route-pin__text']")
