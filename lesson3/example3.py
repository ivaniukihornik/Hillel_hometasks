# DRY, KISS, YAGNI principles
# Don`t repeat yourself
# KISS - Keep it simple, stupid || зроби простіше
# YAGNI - You aren't gonna need it


# ternary operator
a = 10
b = 20
if a > b:
    msg = 'a > b'
else:
    msg = 'a <= b'

msg = 'a > b' if a > b else 'a <= b'  # KISS
print(msg)


# logic operators: and, or
a = 10
b = 20
if a > b:  # and a > 0
    if a > 0:
        msg = 'a > b'
else:
    msg = 'a <= b'

# and
res = a > b and a > 0
# True and True -> True
# True and False -> False
# False and False -> False

res = 1 and '2' and True and 1  # если есть хоть один фолс - выведется первый фолс. если все тру - выведется последний тру
print(res)

# or
if a > b or a > 0:
    msg = 'a > b'
else:
    msg = 'a <= b'


# operations priority
a = 10
b = 20
if (a > b or a > 0) and (a > 10 or b > 0):  # and имеет больший приоритет, чем or
    print('match')

# better to describe one by one
condition1 = a > b or a > 0
condition2 = a > 10 or b > 0

if condition1 and condition2:
    print('match')


# оператор инвертирования
variable = '12345678'

if bool(variable) is True:
    print('variable')

if not variable:
    print('not variable')
else:
    print('variable')


# data type: list

my_str = 'Lorem ipsum dolor amit'
res = my_str.split(' ')
print(res)
print(type(res))

my_str = '''Lorem ipsum do\tlor
amit'''
res = my_str.split()  # split без аргументов разделяет строку во всех местах, которые считает окончанием слова
print(res)


my_list = [0, 1.1, True, 'four', None, [1, 2, 3], 0]  # список данных. Не массив (так как может содержать разные типы данных)
print(my_list)

my_list = []
print(my_list)

my_list.append(1)
print(my_list)
my_list.append('abcde')
print(my_list)

my_list.remove(1)
print(my_list)
print(my_list[0])
print(type(my_list[0].isalpha()))

my_list[0] = True
print(my_list)
my_list.append(False)
print(my_list)

my_list.pop(0)  # удаляет обьект листа по индексу
print(my_list)


my_list += ['a', 'b', 'c']
print(my_list)

my_list *= 2
print(my_list)

print(len(my_list))
print(my_list[5])

my_list.append([1, 2, 3])
print(my_list)

my_list[-1].append(4)
print(my_list)

print(my_list[-1][0:3:1])

if my_list:  # если лист пустой - false
    print(f'list ---> {my_list}')



# loops
# while

c = 10
while c > 5:
    print('True')
    c -= 1


counter = 0

# while True:
#     print(f'Insine loop while {counter}')
#     counter += 1
#     if counter >= 10:
#         break
#
# print(f'Outside loop while {counter}')


while True:
    counter += 1

    if not counter % 2:
        print(counter % 2)
        continue  # заканчивает выполнение цикла для текущего условия

    print(f'Inside loop while {counter}')
    if counter > 10:
        break  # заканчивает выполнение всего цикла

print(f'Outside loop while {counter}')


my_list = ['1', 2, True, None]

idx = 0
limit = len(my_list)
while idx < limit:
    print(my_list[idx])
    idx += 1


# while True:
#     user_input = input('Enter the number: ')
#
#     if user_input.isdigit():
#         print('TNX')
#         break


# for
my_list = ['1', 2, True, None, [1, 2, 3]]

for elem in my_list:
    print(type(elem))
    print(elem)


for i in my_list:  # желательно не добавлять/удалять элементы листа при во время итераций цикла
    if type(i) == bool:
        continue
    print(type(i))

for i in range(10):
    print(type(i))
    print(i)


for i in range(10, 20, 2):
    print(type(i))
    print(i)

lst = ['1', 2, True, None, [1, 2, 3]]

new = lst.copy()
for i in new:
    if type(i) not in (int, float, str):
        lst.remove(i)
        print(lst)
        print(new)