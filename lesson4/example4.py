my_int1 = 1
my_int2 = my_int1

my_int1 += 1
print(id(my_int1))
my_int1 += 1

print(my_int1)
print(my_int2)

print(id(my_int1))
print(id(my_int2))

my_lst1 = [1, 2, 3]
my_lst2 = my_lst1

my_lst2.append(4)

print(my_lst1)
print(my_lst2)

print(id(my_lst1))
print(id(my_lst2))

my_lst1 = [1, 2, 3]
my_lst2 = my_lst1.copy()

my_lst2 = my_lst1[:]

print(my_lst1)
print(my_lst2)

print(id(my_lst1))
print(id(my_lst2))


my_lst1 = [1, 2, 3, ['a', 'b', 'c']]

my_lst2 = my_lst1.copy()

my_lst2[-1].append('d')

print(my_lst1)
print(my_lst2)

print(id(my_lst1[2]))
print(id(my_lst2[2]))


import copy
my_lst1 = ['1000000001', '100000022', '1000000003', ['a', 'b', 'c']]

my_lst2 = copy.deepcopy(my_lst1)

my_lst2[-1].append('d')

print(my_lst1)
print(my_lst2)

print(id(my_lst1[2]))
print(id(my_lst2[2]))

my_bool1 = True
my_bool2 = True

if my_bool1 is my_bool2:  # проверит ссылки обеих элементов, а не их математическое равенство
    pass


# try/except

# 1/0
try:  # рекомендуется использовать только там, где может быть ошибка
    1/0
    print('1/0')
except:
    print('Zero division')


# lst = [1, 2, 3]
#
# try:
#     print(lst[int(input('Enter index: '))])
# except IndexError:
#     print('Exception IndexError')
# except ValueError:
#     print('Exception ValueError')


# lst = [1, 2, 3]
#
# try:
#     print(lst[int(input('Enter index: '))])
# except Exception as e:  #универсальный эксепшн
#     print("Exception")
#     print(f'Exception {e.args}')


# lst = [1, 2, 3]
#
# try:
#     print(lst[10/int(input('Enter index: '))])
# except IndexError:
#     print('Exception IndexError')
# except ValueError:
#     print('Exception ValueError')
# except Exception:
#     print('Exception')


# lst = [1, 2, 3]
#
# try:
#     print(lst[int(input('Enter index: '))])
# except (IndexError, ValueError):
#     print('Exception IndexError ValueError')


# lst = [1, 2, 3]
#
# try:
#     value = lst[int(input('Enter index: '))]
# except (IndexError, ValueError):
#     print('Exception IndexError ValueError')
# except ZeroDivisionError:
#     print('Exception')
# else:
#     print(value)


# lst = [1, 2, 3]
#
# try:
#     value = lst[int(input('Enter index: '))]
# except (IndexError, ValueError):
#     print('Exception IndexError ValueError')
# else:
#     print(value)
# finally:
#     print('Finally')



# data type: tuple - кортеж - immutable data type

my_tuple = (1, 2, 3)
print(my_tuple)
print(my_tuple[1])

for i in my_tuple:
    print(i)

my_tuple = tuple([1, 2, 3, 4])
print(my_tuple)


# data type: set / frozenset. set - mutable data type. frozenset - immutable

my_set = {1, 2, 3, 5}  # - может содержать только immutable типы данных, только уникальные данные
# к элементам сета нельзя обратиться по индексу, можно только по значению

print(my_set)

my_set.add(23)

my_set.remove(1)

print(my_set)

my_set.update({5, 6, 7})
print(my_set)

my_frozenset = frozenset(my_set)

print(my_frozenset)


# data type: dict - mutable data type

my_dict = {}
print(type(my_dict))

my_dict = dict()
print(my_dict)

# данные достаются по ключу
my_dict = {
    1: 100,
    1.2: 2.3,
    False: True,
    None: 'wergh',
    'abcd': [1, 2, 3],
    (1, 2, 3): {1: 2},
    1: 1001
}

print(my_dict['abcd'])
print(my_dict[(1, 2, 3)])
print(my_dict[1])

my_dict['abcd'][0] = 12
print(my_dict)

my_dict[None] = 'None'
print(my_dict)

my_dict.pop(1)
print(my_dict)


my_dict.update({2: 2, 3: 3})
print(my_dict)

my_dict |= {'mnbv': 2222, 3: 4}  # если ключ есть, изменяет. Если нету, добавляет
print(my_dict)

print(my_dict.get(123))  # позволяет спросить, есть ли ключ в дикте и не возвращает None, если нету
print(my_dict.get(123, 'some default value'))  # my_dict[key] if key else 'some default value'


my_dict = {
    1: 100,
    1.2: 2.3,
    False: True,
    None: 'wergh',
    'abcd': [1, 2, 3],
    (1, 2, 3): {1: 2},
    1: 1001
}
for i in my_dict:
    print(i, my_dict[i])

for key in my_dict.keys():  # обращение по ключам
    print(key)
    print(my_dict[key])

for value in my_dict.values(): # по значениям
    print(value)

for item in my_dict.items(): # по ключам и значениям
    print(type(item))  # класс turple
    print(item)

for key, value in my_dict.items():
    print(key)
    print(value)


my_tuple = (1, 2)
a, b = my_tuple  # разпаковка кортежей