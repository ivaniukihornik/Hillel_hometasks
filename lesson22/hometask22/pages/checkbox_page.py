from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from lesson22.hometask22.widgets.checkbox import Checkbox


class CheckboxPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.URL = 'https://demoqa.com/checkbox'
        self.checkbox_loc_value = '//label[contains(@for, "tree-node-{}")]'
        self.checkbox_state_loc_value = self.checkbox_loc_value + '//descendant::*[name()="svg"]' \
                                                                  '[contains(@class, "check")]'
        self.tree_state_loc_value = self.checkbox_loc_value + '//ancestor::li[1][contains(@class, "rct-node-{}")]'
        self.tree_button_loc_value = self.tree_state_loc_value + '//descendant::button'

    def open_page(self):
        self.driver.get(self.URL)

    def __is_collapsed_tree(self, tree_name):
        checkbox = Checkbox(self.driver)
        return checkbox.is_collapsed_tree((By.XPATH, self.tree_state_loc_value.format(tree_name.lower(), 'collapsed')))

    def expand_tree(self, tree: str):
        checkbox = Checkbox(self.driver)
        tree = tree.split('-')
        for tree_top in tree:
            if self.__is_collapsed_tree(tree_top):
                checkbox.expand_tree((By.XPATH, self.tree_button_loc_value.format(tree_top.lower(), '')))

    def expand_trees(self, trees: list):
        for tree in trees:
            self.expand_tree(tree)

    @staticmethod
    def get_checkbox_name(tree: str) -> str:
        return tree.split('-')[-1] if tree.count('-') > 0 else tree

    def get_checkboxes_names(self, trees: list) -> list:
        checkboxes_names = []
        for tree in trees:
            checkboxes_names.append(self.get_checkbox_name(tree))
        return checkboxes_names

    def mark_checkbox(self, checkbox_name: str) -> None:
        checkbox = Checkbox(self.driver)
        checkbox.mark_checkbox((By.XPATH, self.checkbox_loc_value.format(checkbox_name.lower())))

    def mark_checkboxes(self, checkboxes_names: list) -> None:
        for checkbox_name in checkboxes_names:
            self.mark_checkbox(checkbox_name)

    def is_marked_checkbox(self, checkbox_name: str) -> bool:
        checkbox = Checkbox(self.driver)
        return checkbox.is_marked_checkbox((By.XPATH, self.checkbox_state_loc_value.format(checkbox_name.lower())))

    def are_marked_checkboxes(self, checkboxes_names: list) -> bool:
        for checkbox_name in checkboxes_names:
            if not self.is_marked_checkbox(checkbox_name):
                return False
        return True
