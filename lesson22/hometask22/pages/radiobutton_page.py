from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from lesson22.hometask22.widgets.radiobutton import RadioButton


class RadioButtonPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.URL = 'https://demoqa.com/radio-button'
        self.button_locator_value = 'label[for=\'{}Radio\']'
        self.button_status_locator_value = 'input#{}Radio'
        self.buttons_locator = (By.CSS_SELECTOR, 'label[for*=\'Radio\']')

    def open_page(self):
        self.driver.get(self.URL)

    def activate_button(self, name: str) -> None:
        button = RadioButton(self.driver)
        button_locator = (By.CSS_SELECTOR, self.button_locator_value.format(name.lower()))
        button.activate_button(button_locator)

    def is_selected_button_by_prompt(self, name: str) -> bool:
        button = RadioButton(self.driver)
        button_locator = (By.CSS_SELECTOR, self.button_locator_value.format(name.lower()))
        result = button.is_selected_button_by_prompt(name, button_locator)
        return result

    def is_selected_button_by_method(self, name: str) -> bool:
        button = RadioButton(self.driver)
        button_locator = (By.CSS_SELECTOR, self.button_status_locator_value.format(name.lower()))
        result = button.is_selected_button_by_method(button_locator)
        return result

    def get_buttons_info(self) -> dict:
        obj = RadioButton(self.driver)
        buttons_info = obj.get_buttons_info(self.buttons_locator, (By.CSS_SELECTOR, self.button_status_locator_value))
        return buttons_info

    def enable_button(self, name: str) -> None:
        button = RadioButton(self.driver)
        button_locator = (By.CSS_SELECTOR, self.button_status_locator_value.format(name.lower()))
        button.enable_button(button_locator)
