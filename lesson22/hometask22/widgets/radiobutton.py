from selenium.webdriver.remote.webdriver import WebDriver


class RadioButton:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    def activate_button(self, locator: tuple) -> None:
        self.driver.find_element(*locator).click()

    def is_selected_button_by_prompt(self, button: str, locator: tuple) -> bool:
        selected_button = self.driver.find_element(*locator).text.lower()
        return selected_button == button.lower()

    def is_selected_button_by_method(self, locator: tuple) -> bool:
        result = self.driver.find_element(*locator).is_selected()
        return result

    def __is_enabled_button(self, locator: tuple) -> bool:
        result = self.driver.find_element(*locator).is_enabled()
        return result

    def get_buttons_info(self, buttons_locator: tuple, buttons_status_locator: tuple) -> dict:
        buttons_info = {}
        buttons = self.driver.find_elements(*buttons_locator)
        for button in buttons:
            button_name = button.text
            button_status_locator = (buttons_status_locator[0], buttons_status_locator[1].format(button_name.lower()))
            is_enabled = self.__is_enabled_button(button_status_locator)
            is_activated = self.is_selected_button_by_method(button_status_locator)
            buttons_info[button_name] = {'Enabled': is_enabled,
                                         'Activated': is_activated}
        return buttons_info

    def enable_button(self, button_locator: tuple) -> None:
        button = self.driver.find_element(*button_locator)
        self.driver.execute_script('arguments[0].disabled = false', button)
