from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


class Checkbox:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_collapsed_tree(self, locator: tuple) -> bool:
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def expand_tree(self, locator: tuple) -> None:
        self.driver.find_element(*locator).click()

    def mark_checkbox(self, locator: tuple) -> None:
        self.driver.find_element(*locator).click()

    def is_marked_checkbox(self, locator: tuple) -> bool:
        is_marked_attr = self.driver.find_element(*locator).get_attribute('class')
        return is_marked_attr.split('-')[-1] == 'check'
