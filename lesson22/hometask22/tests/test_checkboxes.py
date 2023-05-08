import pytest
from lesson22.hometask22.pages.checkbox_page import CheckboxPage


@pytest.mark.usefixtures('chrome')
@pytest.mark.parametrize('trees', [['Home-Desktop-Commands', 'Home-Documents-Office-General']])
class TestCheckboxes:
    # Написати тест test_checkboxes: на сторінці https://demoqa.com/checkbox обрати (поставити галочку) 2 елемента:
    # Commands (Home-Desktop) та General (Home-Documents-Office). Обирати елементи потрібно однією функцією,
    # за іменем елемента. Як бонусне завдання: реалізувати метод так, щоб він міг приймати масив назв елементів
    # як аргумент і розкривати список послідовно.
    def test_checkboxes(self, trees: list):
        page = CheckboxPage(self.driver)
        page.open_page()
        page.expand_trees(trees)
        checkboxes = page.get_checkboxes_names(trees)
        page.mark_checkboxes(checkboxes)
        assert page.are_marked_checkboxes(checkboxes)
