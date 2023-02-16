# 1
# Напишіть функцію, яка приймає два аргументи.
# Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
# Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
# В будь-якому іншому випадку - функція повертає кортеж з двох агрументів
print('Task 1')


def args_processing (arg1, arg2):
    if type(arg1) in (int, float) and type(arg2) in (int, float):
        result = arg1 * arg2
    elif type(arg1) is str and type(arg2) is str:
        result = f'{arg1} {arg2}'
    else:
        result = (arg1, arg2)
    return result

arg1 = [1, 2, 3]
arg2 = '2'

result = args_processing(arg1, arg2)
print(f'Результат обробки аргументів: {result}')

# 2
# Візьміть попереднє дз "Касир в кінотеатрі" і перепишіть за допомогою функцій. Памʼятайте про SRP!
# Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік
# (можно використати константу або функцію input(), на екран має бути виведено лише одне повідомлення,
# також подумайте над варіантами, коли введені невірні дані).
# якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
# якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
# якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
# у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
print('\n Task 2')


def data_type_processing(entered_data: str):
    if entered_data.isdigit():
        result = int(entered_data)
    elif len(entered_data) == 0:
        result = 'Ви нічого не ввели'
    else:
        result = 'Ви ввели невірні дані'
    return result


def age_processing(age):
    if age >= 0 and age < 7:
        result = 'Де твої батьки?'
    elif age >= 7 and age < 16:
        result = 'Це фільм для дорослих!'
    elif age >= 65 and age <= 125:  # найстарша людина прожила 122,5 роки
        result = 'Покажіть пенсійне посвідчення!'
    elif age >= 16 and age < 65:
        result = 'А білетів вже немає!'
    elif age > 125:
        result = 'Ви ввели невірні дані'
    return result


def is_lucky(age: str):
    if age.count('7') >= 1:
        result = 'Вам сьогодні пощастить!'
        return result

user_age = input('Будь ласка, введіть ваш вік: ')
processed_data = data_type_processing(user_age)
if type(processed_data) is int:
    answer = age_processing(processed_data)
    print(answer)
    is_lucky_answer = is_lucky(user_age)
    if is_lucky_answer is not None:
        print(is_lucky_answer)

else:
    print(processed_data)