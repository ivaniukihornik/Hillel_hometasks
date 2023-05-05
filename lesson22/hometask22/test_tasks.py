import pytest
from lesson22.hometask22.pages.checkbox_page import CheckboxPage
from lesson22.hometask22.pages.radiobutton_page import RadioButtonPage


@pytest.mark.usefixtures('chrome')
@pytest.mark.parametrize('elements', [['Home-Desktop', 'Home-Documents-Office']])
class TestCheckbox:
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


# Написати тести: на сторінці https://demoqa.com/radio-button
@pytest.mark.usefixtures('chrome')
class TestRadioButton:
    # А)(test_activate_yes_radio) Активувати кнопку Yes та переконатись що вона активована. Переконатись двома різними
    # способами.
    def test_activate_yes_radio(self):
        radiobutton = RadioButtonPage(self.driver)
        radiobutton.open_page()
        button_name = 'Yes'
        radiobutton.activate(button_name)
        assert radiobutton.is_selected_by_prompt(button_name) and radiobutton.is_selected_by_method(button_name)

    # Б)(test_get_radio_buttons_info) Визначити які є радіо-баттони на сторінці та сформувати словник із такими даними:
    # Назва кнопки, Чи увімкнена кнопка, Чи активна (обрана) кнопка.
    def test_get_radio_buttons_info(self):
        buttons = RadioButtonPage(self.driver)
        buttons.open_page()
        buttons_info = buttons.get_buttons_info()
        print('\nButtons info:\n', buttons_info)

    # В (Бонус)
    # (test_activate_disabled_radio_button) Увімкнути та активувати кнопку No, переконатись в тому, що вона обрана.
    def test_activate_disabled_radio_button(self):
        button = RadioButtonPage(self.driver)
        button.open_page()
        button_name = 'No'
        button.enable(button_name)
        button.activate(button_name)
        assert button.is_selected_by_method(button_name)
