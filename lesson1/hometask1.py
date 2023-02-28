# 1
# Задача: Створіть дві змінні first=10, second=30.
# Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.
print('Task 1')
first = 10
print(f'first = {first}')
second = 30
print(f'second = {second}')
numbers_summ = first + second
print('first + second =', numbers_summ)
numbers_diff = first - second
print('first - second =', numbers_diff)
numbers_prod = first * second
print('first * second =', numbers_prod)
numbers_float_div = first / second
print('first / second =', numbers_float_div)
numbers_exp = first ** second
print('first ** second =', numbers_exp)
numbers_int_div = first // second
print('first // second =', numbers_int_div)
numbers_div_remainder = first % second
print('first % second =', numbers_div_remainder)

# 2
# Задача: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння.
print('\nTask 2')
comparing_result = first < second
print('Is first < second? -', comparing_result)
comparing_result = first > second
print('Is first > second? -', comparing_result)
comparing_result = first == second
print('Is first == second? -', comparing_result)
comparing_result = first != second
print('Is first != second? -', comparing_result)

# 3
# Задача: Створіть змінну - резкльтат конкатенації строк "Hello " та "world!".
str1 = 'Hello '
str2 = 'world!'
concatenation_result = str1 + str2