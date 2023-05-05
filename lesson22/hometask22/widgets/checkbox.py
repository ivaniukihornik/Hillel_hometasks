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

    def expand_tree(self, tree_button_locator: str) -> None:
        self.driver.find_element(By.XPATH, tree_button_locator).click()

    def mark_checkboxes(self, tree_state_locator: str, tree_button_locator: str, checkbox_locator: str, names: list)\
            -> None:
        for name in names:
            elements = name.split('-')
            for element in elements:
                if self.__is_collapsed(tree_state_locator, element):
                    self.expand_tree(tree_button_locator.format(element.lower(), ''))
            checkbox = self.driver.find_element(By.XPATH, checkbox_locator.format(elements[-1].lower()))
            checkbox.click()

    def are_marked(self, locator: str, names: list) -> bool:
        for name in names:
            is_marked_attr = self.driver.find_element(By.XPATH, locator.format(name.lower())).get_attribute('class')
            is_marked = is_marked_attr.split('-')[-1]
            result = True if is_marked == 'check' else False
            if not result:
                return False
        return True