from selenium.webdriver.remote.webdriver import WebDriver
from lesson26.hometask.widgets.dynamic_properties import Button


class DynamicPropertiesPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    __url = 'https://demoqa.com/dynamic-properties'
    __button_locator = 'button#{}'

    def open_page(self):
        self.driver.get(self.__url)

    def is_button_enabled(self, button_name: str):
        button = Button(self.driver)
        return button.is_button_enabled(self.__button_locator.format(button_name))

    def has_button_color_changed(self, button_name: str):
        button = Button(self.driver)
        return button.has_button_changed_color(self.__button_locator.format(button_name))

    def is_button_visible(self, button_name: str):
        button = Button(self.driver)
        return button.is_button_visible(self.__button_locator.format(button_name))