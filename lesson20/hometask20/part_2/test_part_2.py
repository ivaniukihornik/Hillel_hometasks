# 3 тести, знаходяться поза класом (в тестовому файлі взагалі відсутній клас). На кожному тесті -- мітка 'param'.
# Тести мають бути параметризовані: перший протестує одиночні параметри, другий -- подвійні, третій -- одиночні,
# але з присвоєнням псевдонімів. На кожен тест має діяти фікстура, що знаходиться на рівні проекту та виводить
# повідомлення перед та після кожного тесту. В сигнатурі тесту має бути пусто (не викликати фікстуру примусово).
from pytest import mark
import lesson20.hometask20.part_2.weather_page as page_weather  # імпортував через повний шлях, бо раніше видалив модуль
# з таким же іменем, і виникав ModuleNotFoundError, якщо імпортувати не через повний


@mark.param
@mark.parametrize('city', ['Киев', 'Барселона', 'Мюнхен', 'Дубай'])
def test_is_warm_now(city):
    page_weather.open_page()
    page_weather.fill_search_field(city)  # ввожу потрібне місто
    page_weather.submit_search()
    today_temp = page_weather.get_now_temp(city.lower())  # отримую поточну температуру в місті
    assert today_temp >= 15


# деякі назви міст повторюються, тому для уточнення потрібно вказувати регіон
@mark.param
@mark.parametrize('city, region', [['Йорк', 'Небраска'], ['Каховка', 'Одесская обл.'], ['Александрия', 'Египет']])
def test_is_cold_now(city, region):
    page_weather.open_page()
    page_weather.fill_search_field(city)  # ввожу потрібне місто
    page_weather.choose_search_result(region)
    today_temp = page_weather.get_now_temp(city.lower())
    assert today_temp < 10


@mark.param
@mark.parametrize('city', ['Осло', 'Лондон', 'Оттава'],
                  ids=['CAPITAL OF NORWAY', 'CAPITAL OF ENGLAND', 'CAPITAL OF CANADA'])
def test_is_raining_now(city):
    page_weather.open_page()
    page_weather.fill_search_field(city)  # ввожу потрібне місто
    page_weather.submit_search()
    weather_now = page_weather.get_weather_by_img()  # отримую поточну температуру в місті
    assert weather_now.lower().__contains__('дождь')