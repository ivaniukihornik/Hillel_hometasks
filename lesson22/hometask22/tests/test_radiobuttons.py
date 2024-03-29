import pytest
from lesson22.hometask22.pages.radiobutton_page import RadioButtonPage


# Написати тести: на сторінці https://demoqa.com/radio-button
@pytest.mark.usefixtures('chrome')
class TestRadioButtons:
    # А)(test_activate_yes_radio) Активувати кнопку Yes та переконатись що вона активована. Переконатись двома різними
    # способами.
    def test_activate_yes_radio(self):
        page = RadioButtonPage(self.driver)
        page.open_page()
        button_name = 'Yes'
        page.activate_button(button_name)
        is_selected_button_by_prompt = page.is_selected_button_by_prompt(button_name)
        is_selected_button_by_method = page.is_selected_button_by_method(button_name)
        assert all([is_selected_button_by_prompt, is_selected_button_by_method])

    # Б)(test_get_radio_buttons_info) Визначити які є радіо-баттони на сторінці та сформувати словник із такими даними:
    # Назва кнопки, Чи увімкнена кнопка, Чи активна (обрана) кнопка.
    def test_get_radio_buttons_info(self):
        page = RadioButtonPage(self.driver)
        page.open_page()
        buttons_info = page.get_buttons_info()
        print('\nButtons info:\n', buttons_info)

    # В (Бонус)
    # (test_activate_disabled_radio_button) Увімкнути та активувати кнопку No, переконатись в тому, що вона обрана.
    def test_activate_disabled_radio_button(self):
        page = RadioButtonPage(self.driver)
        page.open_page()
        button_name = 'No'
        page.enable_button(button_name)
        page.activate_button(button_name)
        assert page.is_selected_button_by_method(button_name)
