from selenium.webdriver.remote.webdriver import WebDriver


class RadioButton:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def activate(self, locator: tuple) -> None:
        self.driver.find_element(*locator).click()

    def is_selected_by_prompt(self, button: str, locator: tuple) -> bool:
        selected_button = self.driver.find_element(*locator).text.lower()
        return True if selected_button == button.lower() else False

    def is_selected_by_method(self, locator: tuple) -> bool:
        result = self.driver.find_element(*locator).is_selected()
        return result

    def __is_enabled(self, locator: tuple) -> bool:
        result = self.driver.find_element(*locator).is_enabled()
        return result

    def get_buttons_info(self, buttons_locator: tuple, buttons_status_locator: tuple) -> dict:
        buttons = self.driver.find_elements(*buttons_locator)
        buttons_info = {}
        for button in buttons:
            button_name = button.text
            button_status_locator = (buttons_status_locator[0], buttons_status_locator[1].format(button_name.lower()))
            is_enabled = 'Enabled' if self.__is_enabled(button_status_locator) else 'Disabled'
            is_activated = 'Activated' if self.is_selected_by_method(button_status_locator) else 'Deactivated'
            buttons_info[button_name] = f'{is_enabled} and {is_activated}'
        return buttons_info

    def enable(self, button_locator: tuple) -> None:
        button = self.driver.find_element(*button_locator)
        self.driver.execute_script('arguments[0].disabled = false', button)