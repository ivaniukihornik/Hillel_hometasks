import pytest
from lesson22.hometask22.pages.checkbox_page import CheckboxPage


@pytest.mark.usefixtures('chrome')
@pytest.mark.parametrize('elements', [['Home-Desktop', 'Home-Documents-Office']])
class TestCheckboxes:
    # Написати тест test_checkboxes: на сторінці https://demoqa.com/checkbox обрати (поставити галочку) 2 елемента:
    # Commands (Home-Desktop) та General (Home-Documents-Office). Обирати елементи потрібно однією функцією,
    # за іменем елемента. Як бонусне завдання: реалізувати метод так, щоб він міг приймати масив назв елементів
    # як аргумент і розкривати список послідовно.
    def test_checkboxes(self, elements: list):
        checkbox = CheckboxPage(self.driver)
        checkbox.open_page()
        checkbox.mark_checkboxes(elements)
        checkbox_names = []
        for checkbox_full_name in elements:
            checkbox_name = checkbox_full_name.split('-')[-1] if checkbox_full_name.count('-') > 0 \
                else checkbox_full_name
            checkbox_names.append(checkbox_name)
        assert checkbox.are_marked(checkbox_names)