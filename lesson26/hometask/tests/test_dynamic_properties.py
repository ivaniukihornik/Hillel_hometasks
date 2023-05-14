import pytest
from lesson26.hometask.pages.dynamic_properties import DynamicPropertiesPage


@pytest.mark.usefixtures('chrome')
class TestDynamicProperties:
    """На сторінці https://demoqa.com/dynamic-properties зробити 3 тести"""
    def test_enable_after_btn(self):
        """Переконується що кнопка "Enable after" вмикається"""
        button = 'enableAfter'
        page = DynamicPropertiesPage(self.driver)
        page.open_page()
        assert page.is_button_enabled(button)

    def test_color_change_btn(self):
        """Переконується що колір напису на кнопці "Color change" змінюється"""
        button = 'colorChange'
        page = DynamicPropertiesPage(self.driver)
        page.open_page()
        assert page.has_button_color_changed(button)

    def test_visible_after_btn(self):
        """Переконується, що кнопка "Visible after" з'являється на сторінці"""
        button = 'visibleAfter'
        page = DynamicPropertiesPage(self.driver)
        page.open_page()
        assert page.is_button_visible(button)
