# 1
# Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
# Напишіть код, який видалить (не створить новий, а саме видалить!) з нього всі числа, які менше 21 і більше 74.
print('Task 1')
numbers_list = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]
print('Initial list: {}'.format(numbers_list))
for index in reversed(range(len(numbers_list))):
    list_element = numbers_list[index]
    if list_element < 21 or list_element > 74:
        numbers_list.remove(list_element)
print('Result list after deleting numbers which less than 21 and more than 74: {}'.format(numbers_list))



# 2
# Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245,
# "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "roze-tka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких потрапляють в діапазон між мінімальною і максимальною ціною.
# Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"
print('\nTask 2')
stores_prices = {
    'cito': 47.999,
    'BB_studio': 42.999,
    'momo': 49.999,
    'main-service': 37.245,
    'buy.now': 38.324,
    'x-store': 37.166,
    'the_partner': 38.988,
    'store': 37.720,
    'roze-tka': 38.003
}
lower_limit = 38.228
upper_limit = 45.345
match = ''
for item in stores_prices.items():
    item_price = item[1]
    if item_price > lower_limit and item_price < upper_limit:
        match += item[0] + ', '
print('Stores with prices between {} and {}: {}'.format(lower_limit, upper_limit, match.rstrip(', ')))