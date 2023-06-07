# Знайдіть публічне API, яке вам цікаво. Наприклад, ви можете використати API GitHub, API курсів валют або будь-яке
# інше публічне API, яке вам подобається.
# Встановіть бібліотеку requests, якщо вона ще не встановлена. Ви можете встановити її за допомогою команди
# pip install requests.
# Створіть Python-скрипт, який містить функцію або клас для кожного з наступних завдань:
from requests import get, post
import json

URL = 'https://favqs.com/'


# a. Отримання інформації з API: Напишіть функцію або метод, який виконує GET-запит до API і повертає відповідь сервера.
# Ви можете використати метод requests.get() для цього. Виведіть отримані дані на екран або збережіть їх у файл.
def get_info_from_api():
    """Obtains a random quote from API and returns the quote and its data in json"""
    end_point = 'api/qotd'
    response = json.loads(get(url=URL+end_point).text)
    return response


print(f'\nTask a\nYou have successfully got a quote of the day!\nQuote: {get_info_from_api()["quote"]["body"]}'
      f'\nAuthor: {get_info_from_api()["quote"]["author"]}')


# b. Надсилання даних на API: Напишіть функцію або метод, який виконує POST-запит до API з деякими вхідними даними і
# повертає відповідь сервера. Ви можете використати метод requests.post() для цього. Виведіть отримані дані на екран
# або збережіть їх у файл.
def create_user_session_with_api():
    """Creates a users session and returns users token in case of success. Othervise returns error code and message"""
    end_point = 'api/session'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token token="79d302926572faa1dca2d21ac5e1cf59"',
    }
    request_body = {
        "user": {
            "login": "ivaniukihornik@gmail.com",
            "password": "fe99f37ff87eb"
        }
    }
    request_body_json = json.dumps(request_body)
    response = post(url=URL+end_point, data=request_body_json, headers=headers)
    try:
        return f'You have successfully created a user session! Your session token is below:' \
               f'\n{json.loads(response.text)["User-Token"]}'
    except KeyError:
        return json.loads(response.text)


print(f'\nTask b\n{create_user_session_with_api()}')


# c. Параметризоване тестування: Напишіть функцію або метод, який приймає параметри (наприклад, URL, метод,
# тіло запиту) і виконує відповідний запит до API. Використовуйте параметри, які надаються як аргументи функції або
# методу. Поверніть результат виконання запиту.
def create_user_with_api(login: str, email: str, password: str):
    """Obtains users data and creates user with API.
    In case of success returns users data. Othervise rerutns error code with message"""
    end_point = 'api/users'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Token token="79d302926572faa1dca2d21ac5e1cf59"',
    }
    request_body = {
            "user": {
                "login": login,
                "email": email,
                "password": password
            }
        }
    request_body_json = json.dumps(request_body)
    response = post(url=URL+end_point, data=request_body_json, headers=headers)
    return json.loads(response.text)


print(f'\nTask c'
      f'\n{create_user_with_api(login="ihor_6", email="ivaniukihornik+6@gmail.com", password="12345")}')
