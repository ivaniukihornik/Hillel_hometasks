# 1. Створити тест за допомогою Selenium IDE
# 2. Експортувати в python
# 3. Запустити тест
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAddingToCart():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_adding_to_cart(self):
        self.driver.get("https://rozetka.com.ua/ua/asus-90nr0667-m00kt0/p362023689/")
        self.driver.maximize_window()
        time.sleep(2)

        # запам'ятовую назву та ціну товару з його сторінки
        page_product_name = self.driver.find_element(By.CLASS_NAME, 'product__title').text
        page_product_price = self.driver.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]'
                                                                '/rz-product-main-info/div[1]/div[1]/div[1]/p[2]').text

        # додаю товар у кошик
        self.driver.find_element(By.XPATH, '//*[@id="#scrollArea"]/div[1]/div[2]/rz-product-main-info'
                                           '/div[1]/div[1]/rz-product-buy-btn/app-buy-button/button').click()
        time.sleep(2)

        # запам'ятовую назву та ціну товару з кошику
        cart_product_name = self.driver.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window'
                                                               '/div[3]/div[2]/rz-shopping-cart/div/rz-purchases/ul/li'
                                                               '/rz-cart-product/div/div[1]/div/a').text
        cart_product_price = self.driver.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]'
                                                                '/div[2]/rz-shopping-cart/div/rz-purchases/ul/li'
                                                                '/rz-cart-product/div/div[2]/div/p[2]').text

        # Порівнюю дані зі сторінки товару з даними з кошику. Якщо співпадають - додавання в кошик працює
        assert page_product_name == cart_product_name and page_product_price == cart_product_price




