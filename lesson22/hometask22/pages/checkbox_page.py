from selenium.webdriver.remote.webdriver import WebDriver
from lesson22.hometask22.widgets.widgets import Checkbox


class CheckboxPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.URL = 'https://demoqa.com/checkbox'
        self.checkbox_locator = '//label[contains(@for, "tree-node-{}")]'
        self.checkbox_state_locator = self.checkbox_locator + '//descendant::*[name()="svg"][contains(@class, "check")]'
        self.tree_state = self.checkbox_locator + '//ancestor::li[1][contains(@class, "rct-node-{}")]'
        self.tree_button = self.tree_state + '//descendant::button'

    def open_page(self):
        self.driver.get(self.URL)

    def mark_checkboxes(self, full_names: list) -> None:
        checkbox = Checkbox(self.driver)
        checkbox.mark_checkboxes(self.tree_state, self.tree_button, self.checkbox_locator, full_names)

    def are_marked(self, full_names: list) -> bool:
        checkbox = Checkbox(self.driver)
        return checkbox.are_marked(self.checkbox_state_locator, full_names)
