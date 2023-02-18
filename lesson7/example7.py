# def my_function(arg1, arg2=10, *args, **kwargs):
#     print(arg1, arg2)
#     result = arg1 + arg2
#     return result
#
# #
# # value = my_function(1, 2)
# # value = my_function(1)
#
#
# def my_next_function(arg1, arg2):
#     print(arg1, arg2)
#     result = my_function(arg1 + arg2)
#     return result
#
#
# my_next_function(10, 20)
#
# print(type(my_next_function))


# global_value = 100

# print(dir())

# for name in dir(__builtins__):
#     print(name)


# global_value = 100
#
#
# def foo(arg1, arg2):
#     # global_value = 200
#     global_value += 200
#     print(global_value)
#
#
# print('before function global_value is :', global_value)
# foo(1, 2)
# print('after function global_value is :', global_value)


# global_value = [100]


# def foo(arg1, arg2):
#     # global_value = 200
#     global_value.append(200)
#     print(global_value)
#
#
# global_value = [100]
#
# print('before function global_value is :', global_value)
# foo(1, 2)
# print('after function global_value is :', global_value)

# PI = 3.1415
#
#
# def foo(arg1, arg2, global_list):
#     global_list.append(200)
#     print(global_list)
#     return global_list
#
#
# global_value = [100]
#
# print('before function global_value is :', global_value)
# global_value = foo(1, 2, global_value)
# print('after function global_value is :', global_value)


# global_value = 100
#
#
# def foo(arg1, arg2):
#     global global_value
#     global_value += 200
#     print(global_value)
#
#
# print('before function global_value is :', global_value)
# foo(1, 2)
# print('after function global_value is :', global_value)


# global_value = 100
#
#
# def foo():
#     print(global_value)
#     a = 100
#     return a
#
#
# print('before function global_value is :', global_value)
# foo()
# print('after function global_value is :', global_value)
# a = foo()
# foo()
#
# del global_value
#
# foo()


# def my_function(arg1, arg2):
#     """
#     Bla-bla-bla
#     Bla-bla-bla
#     Bla-bla-bla
#     Bla-bla-bla
#
#     :param arg1: Bla-bla-bla
#     :type arg1: int
#     :param arg2: Bla-bla-bla
#     :type arg2: str
#     :return: Bla-bla-bla
#     :rtype: int
#     """
#     return 1
#
#
# res = my_function('2', 1)
#
# my_function(1, res)
#
#
# def my_function(arg1, arg2):
#     """
#     Bla-bla-bla
#
#     Args:
#         arg1 (int):
#         arg2 (float):
#
#     Returns:
#         (str):
#     """
#     return '1'


# def my_function(arg1: int, arg2: float = 2.3) -> str:
#     """"""
#     print(arg1)
#     print(arg2)
#     return '1'
#
#
# my_function('asdf', 'sss')


# f = !5

# f = 5 * 4 * 3 * 2 * 1
# f = 5 * !4
# f = 5 * 4 * !3

# f = !n
# f = n * (n-1) * (n-2) .... * 1

# f(5) -> 5 * f(4)

# counter = 0
#
#
# def factorial_rec(number):
#
#     global counter
#     counter += 1
#     if number <= 1:
#         return 1
#
#     return number * factorial_rec(number - 1)
#
#
# n = 55
#
#
# res = factorial_rec(n)
#
# print(res)
# print(counter)


# n[x] = n[x-1] + n[x-2]

# 1 1 2 3 5 8 13 21 34 55 89 .....

# counter = 0

#
# def fib_rec(number):
#
#     global counter
#     counter += 1
#     if number in (1, 2):
#         return 1
#
#     return fib_rec(number - 1) + fib_rec(number - 2)
#
#
# print(fib_rec(30))  # O(n**2)
# print(counter)

# counter = 0


# def fib_plain(number):
#
#     global counter
#     counter += 1
#
#     fib1 = fib_2 = 1
#
#     if number in (1, 2):
#         return fib_2
#
#     for i in range(number - 2):
#
#         fib1, fib_2 = fib_2, fib1 + fib_2
#
#     return fib_2


# print(fib_plain(400))
# print(counter)


# lst = [1, 2, ['a', 'b'], 3, [1, 2, 3, [1, 2, 3]]]

# for i in lst:
#     print(i)
#     if isinstance(i, list):
#         for j in i:
#             print(j)


# def dig_into_list(lst):
#     for list_item in lst:
#         if isinstance(list_item, list):
#             dig_into_list(list_item)
#         else:
#             print(list_item)
#
#
# dig_into_list(lst)


# for i in dir(__builtins__):
#     print(i)


# int
# float
# str
# bool

# list
# tulple
# dict
# set
# frozenset

# my_dict = dict()
# print(my_dict)
#
# my_dict = dict(
#     a=10,
#     b=20,
# )
#
# print(my_dict)
#
#
# data = [('two', 2), ((0, 1), 1), (None, 3), (True, 5)]
#
# my_dict = dict(data)
#
# print(my_dict)

# math

# my_value = max(1, 2, 3)
# print(my_value)


# my_value = max([1, 3, 2, 3])
# print(my_value)


# def foo(n):
#     return n % 3
#
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# # my_value = max(lst, key=foo)
# #
# # print(my_value)
# #
# #
# # my_value = min(lst, key=foo)
# #
# # print(my_value)
#
# print(sum(lst))
#
#
# for i in range(1, 10, 2):
#     print(i)

#
# my_str = set('Lorem ipsum')
#
# enum = enumerate(my_str)
#
# for i in enum:
#     print(i)
#
# print(dict(enumerate('asdfghjk')))


# def foo(val):
#     return (val + 1) ** 2
#
#
# data = (1, 2, 3, 4, 5)
#
# for i in map(foo, data):
#     print(i)
#
#
# for i in data:
#     i = foo(i)
#     print(i)
#


# data1 = (1, 2, 3, 4, 5)
# data2 = 'asdfghjkl;'
# data3 = '_)(*&^%$#@'
#
# ziped = zip(data1, data2, data3)
#
#
# for i in ziped:
#     print(i)

data1 = (1, 22, 44, 66, 1, 4, 2, 3, 4, 5)


def foo(val):
    return val % 3


res = list(sorted(data1, key=foo, reverse=True))
print(res)


res = list(sorted(data1, key=lambda value: value % 3, reverse=True))
print(res)


# lambda *args, **kwargs: # smth args kwargs

my_lambda = lambda value: value % 3  # bad idea, use function


res = list(sorted(['1', '3.5', '2', '100'], key=lambda x: float(x)))  # bad idea, use float function

print(res)

res = list(sorted(['1', '3.5', '2', '100'], key=float))

print(res)

res = list(sorted(['1', '3.5', '2', '100'], key=lambda x: float(x) ** 0.5))

print(res)


data = [3, 5, 1, 88, 22, 7, 54, 3, 1]

filtered = filter(lambda x: x % 2 == 0, data)

print(list(filtered))
