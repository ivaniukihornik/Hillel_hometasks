# 1
# Напишіть функцію, яка визначає сезон за датою. Функція отримує стрінг у форматі "[день].[місяць]"
# (наприклад "12.01", "30.08", "1.11" і тд) і повинна повернути стрінг з відповідним сезоном,
# до якого відноситься ця дата ("літо", "осінь", "зима", "весна")
print('Task 1')
import re

def data_checking(data: str):
    '''Receives a data and verifies if it matches the format: "[day].[month]".'''
    if data.count('.') == 1:
        day_len = len(data.split('.')[0])
        month_len = len(data.split('.')[1])
        if day_len in (1, 2) and month_len == 2:
            check_result = bool(re.match(r'(([1-9]|0[1-9]|[1-2][0-9]|3[0-1])\.(01|03|05|07|08|10|12))|'  # регулярка для місяців, що містять 31 день
                      r'(([1-9]|0[1-9]|[1-2][0-9]|30)\.(04|06|09|11))|'  # регулярка для місяців з 30 днями
                      r'(([1-9]|0[1-9]|[1-2][0-9])\.(02))', data))  # регулярка для лютого
        else:
            check_result = False
    else:
        check_result = False
    return check_result

def season_determination(date: str):
    '''Receives a date in format "[day].[month]" and determines a season which this date relates.'''
    month_str = date.split('.')[1]
    month_int = int(month_str)
    if month_int in (3, 4, 5):
        season = 'Spring'
    elif month_int in (6, 7, 8):
        season = 'Summer'
    elif month_int in (9, 10, 11):
        season = 'Autumn'
    else:
        season = 'Winter'
    return season

entered_date = input('Please enter a date: ')

while True:
    if data_checking(entered_date) is False:
        entered_date = input('Bad date format or invalid date. Repeat entering: ')
    else:
        break

returned_season = season_determination(entered_date)
print(f'This date relates to: {returned_season}')


# 2
# Напишіть функцію "Тупий калькулятор", яка приймає два числових аргументи і строковий,
# який відповідає за операцію між ними (+ - / *).
# Функція повинна повертати значення відповідної операції (додавання, віднімання, ділення, множення),
# інші операції не допускаються.
# Якщо функція оримала невірний тип данних для операції (не числа) або неприпустимий (невідомий) тип операції,
# вона повинна повернути None і вивести повідомлення "Невірний тип даних" або "Операція не підтримується" відповідно.


print('\nTask 2')

def stupid_calculator(num1_str: str, num2_str: str, oper: str):
    '''Receives two numbers and arithmetical operation in string type.
        Converts numbers into "float" type and returns the result of received operation between them.

        In case of obtaining invalid data types returns "None" and displays error message(s).
        '''
    if num1_str.replace('.', '').isdigit() and num2_str.replace('.', '').isdigit() is False:
        print('Invalid data type')
        if oper != '+' and oper != '-' and oper != '*' and oper != '/':
            print('Operation not supported!')
        result = None
    else:
        num1 = float(num1_str)
        num2 = float(num2_str)
        if oper == '+':
            result = num1 + num2
        elif oper == '-':
            result = num1 - num2
        elif oper == '*':
            result = num1 * num2
        elif oper == '/':
            result = num1 / num2
        else:
            print('Operation not supported!')
            result = None
    return result

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
operation = input('Enter the desired operation between numbers: ')

operation_result = stupid_calculator(number1, number2, operation)
print(f'The result of operation "{operation}" between numbers "{number1}" and "{number2}": {operation_result}')