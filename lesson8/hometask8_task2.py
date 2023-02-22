# 2
# Візьміть функції з попереднього ДЗ, покладіть їх у файл lib.py і імпортуйте в основний файл для виконання
import lib
# 2.1
# Напишіть функцію, яка визначає сезон за датою. Функція отримує стрінг у форматі "[день].[місяць]"
# (наприклад "12.01", "30.08", "1.11" і тд) і повинна повернути стрінг з відповідним сезоном,
# до якого відноситься ця дата ("літо", "осінь", "зима", "весна")

print('Task 2.1')
entered_date = input('Please enter a date: ')

while True:
    if lib.data_checking(entered_date) is False:
        entered_date = input('Bad date format or invalid date. Repeat entering: ')
    else:
        break

returned_season = lib.season_determination(entered_date)
print(f'This date relates to: {returned_season}')


# 2.2
# Напишіть функцію "Тупий калькулятор", яка приймає два числових аргументи і строковий,
# який відповідає за операцію між ними (+ - / *).
# Функція повинна повертати значення відповідної операції (додавання, віднімання, ділення, множення),
# інші операції не допускаються.
# Якщо функція оримала невірний тип данних для операції (не числа) або неприпустимий (невідомий) тип операції,
# вона повинна повернути None і вивести повідомлення "Невірний тип даних" або "Операція не підтримується" відповідно.

print('\nTask 2.2')
number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
operation = input('Enter the desired operation between numbers: ')

operation_result = lib.stupid_calculator(number1, number2, operation)
print(f'The result of operation "{operation}" between numbers "{number1}" and "{number2}": {operation_result}')