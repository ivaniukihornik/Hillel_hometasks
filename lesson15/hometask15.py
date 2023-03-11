# Підключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ),
# отримайте курс валют і запишіть його в текстовий файл такому форматі (список):
#
# "[дата створення запиту]"
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
# ...
# n. [назва валюти n] to UAH: [значення курсу до валюти n]
# P.S.не забувайте про DRY, KISS, SRP та перевірки
from datetime import datetime
import requests


def text_creator(date: str, data: dict):
    """Obtains date and data values.
    Creates and returns a string with currencies exchange rates to UAH from obtained data on obtained date"""
    res_text = f'{date}'
    counter = 1
    for currency in data:
        curr_name = currency['CurrencyCodeL']
        curr_units = currency['Units']
        curr_amount = currency['Amount']
        curr_total_amount = round((curr_amount / curr_units), 4)
        res = f'{counter}. {curr_name} to UAH: {curr_total_amount}'
        counter += 1
        res_text += '\n' + res
    return res_text


def text_writer(name: str, data: str):
    """Obtains data and filename in string formats and writes data to file"""
    with open(name, 'w') as file:
        file.write(data)


def data_checker(date: str, data: dict):
    """Obtains data and date.
    Compares dates from data lines with obtained date and returns the result of comparison
    (if at least one comparison is false - result is false)"""
    for line in data:
        line_date = line['StartDate']
        res = line_date == date
        if res is False:
            break
        return res


today = datetime.now().strftime('%d.%m.%Y')
exchange_url = f'https://ba1nk.gov.ua/NBU_Exchange/exchange?json&date={today}'
file_name = 'exchange_rates.txt'

try:
    requests.get(exchange_url)
except:
    print('URL error')
    exit()

url_data = requests.get(exchange_url)
if url_data.status_code == 200:
    try:
        url_data.json()
    except:
        print('URL data error')
        exit()

json_data = url_data.json()
check_data = data_checker(today, json_data)
if check_data is False:
    print('JSON data error')
else:
    text = text_creator(today, json_data)
    text_writer(file_name, text)
    print(f'File "{file_name}" with currencies exchange rates to UAH on {today} was successfully created!')