from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

driver = webdriver.Chrome()
URL = 'https://sinoptik.ua/'

now_temp = (By.CSS_SELECTOR, 'p.today-temp')
search_field = (By.ID, 'search_city')
search_button = (By.CSS_SELECTOR, 'p > input.search_city-submit')
search_results_bar = (By.CSS_SELECTOR, '.ac_results')
img_weather = (By.CSS_SELECTOR, '.img>img')


def open_page():
    driver.delete_all_cookies()
    driver.get(URL)


def get_now_temp(city: str) -> int:
    WebDriverWait(driver, 5).until(ec.url_contains(URL + quote('погода-' + city)))
    temp = driver.find_element(*now_temp).text
    temp_value = int(temp.rstrip('°C'))
    return temp_value


def fill_search_field(text: str) -> None:
    driver.find_element(*search_field).send_keys(text)


def submit_search() -> None:
    driver.find_element(*search_button).click()


def choose_search_result(name: str) -> None:
    search_result = (By.XPATH, f'//div/ul/li/span[contains(text(), \'{name}\')]')
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(search_results_bar))
    driver.find_element(*search_result).click()


def get_weather_by_img() -> str:
    WebDriverWait(driver, 5).until(ec.visibility_of_element_located(img_weather))
    weather_state = driver.find_element(*img_weather).get_attribute('alt')
    return weather_state
