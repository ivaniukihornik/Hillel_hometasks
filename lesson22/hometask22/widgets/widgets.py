from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Checkbox:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def __is_collapsed(self, locator: str, name: str) -> bool:
        try:
            self.driver.find_element(By.XPATH, locator.format(name.lower(), 'collapsed'))
            return True
        except NoSuchElementException:
            return False

    def mark_checkboxes(self, tree_state_locator: str, tree_button_locator: str, checkbox_locator: str, names: list)\
            -> None:
        for name in names:
            elements = name.split('-')
            for element in elements:
                if self.__is_collapsed(tree_state_locator, element):
                    self.driver.find_element(By.XPATH, tree_button_locator.format(element.lower(), '')).click()
            checkbox = self.driver.find_element(By.XPATH, checkbox_locator.format(elements[-1].lower()))
            checkbox.click()

    def are_marked(self, locator: str, names: list) -> bool:
        for name in names:
            is_marked_attr = self.driver.find_element(By.XPATH, locator.format(name.lower())).get_attribute('class')
            is_marked = is_marked_attr.split('-')[-1]
            result = True if is_marked == 'check' else False
            if result is False:
                return False
        return True


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
