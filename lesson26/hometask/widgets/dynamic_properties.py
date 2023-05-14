from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Button:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__wait = WebDriverWait(driver, 10, 1)

    def is_button_enabled(self, locator: str):
        try:
            button:WebElement = self.__wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
            return button.is_enabled()
        except TimeoutException:
            return False

    def has_button_changed_color(self, locator: str):
        try:
            self.__wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator + '[class*="text-danger"]')))
            return True
        except TimeoutException:
            return False

    def is_button_visible(self, locator: str):
        try:
            self.__wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False
