# import random
#
# print(dir())
#
# print(random.randint(1, 10))


# from random import randint
#
# print(randint(1, 10))


# import random as RANDOM
#
# print(dir())
#
# print(RANDOM.randint(1, 10))


# from random import randint as RI
#
# print(RI(1, 10))


# import random, os
#
# import random
# import os


# from random import random
# from random import randint as RI, choice as CHOICE
#
# from random import (
#     randint as RI,
#     choice as CHOICE,
# )
#
#
# print(random())
# print(RI(1, 20))
# print(CHOICE([1, 2, 3]))

# print(dir())

# from random import *  # random, randint ...
#
# print(dir())
#
# import requests


# import lib
#
# print(lib.var2)
#
# lib.foo()


# from lib import foo as FOO
#
# FOO()

# a = 10
#
# print('im example.py', __name__)
#
#
# import lib  # python3 lob.py


# decorator


# def foo():
#     print('FUNCTION FOO')
#
#
# print(id(foo))
#
#
# def bar(func):
#     func()
#
#
# bar(foo)


# def spam():
#
#     def my_function():
#         print('My function')
#
#     return my_function
#
#
# res = spam()
#
# print(res)
#
# res()


# def some_function(*args, **kwargs):
#     print('I\'m a function `some_function`')
#     print(args, kwargs)
#
#
# def function_wrapper(func):
#
#     def _wrapper(*args, **kwargs):
#
#         print('Before function')
#         res = func(*args, **kwargs)
#         print('After function')
#
#         return res
#
#     return _wrapper
#
#
# # wrapped_function = function_wrapper(some_function)
#
# # some_function()
# # wrapped_function()
#
# some_function = function_wrapper(some_function)
#
#
# some_function()


# def function_wrapper(func):
#
#     def _wrapper(*args, **kwargs):
#
#         print('Before function')
#         res = func(*args, **kwargs)
#         print('After function')
#
#         return res
#
#     return _wrapper
#
#
# @function_wrapper  # some_function = function_wrapper(some_function)
# def some_function(*args, **kwargs):
#     print('I\'m a function `some_function`')
#     print(args, kwargs)
#
#     return 10
#
#
# res = some_function(10, a='12345')

#
# def type_checker_int(func):
#
#     def _wrapper(*args, **kwargs):
#         print('Inside `type_checker_int`')
#         for arg in args:
#             if not isinstance(arg, int):
#                 raise TypeError
#         for kwarg in kwargs.values():
#             if not isinstance(kwarg, int):
#                 raise TypeError
#         res = func(*args, **kwargs)
#         return res
#
#     return _wrapper
#
#
# @type_checker_int
# def some_function(*args, **kwargs):
#     print('I\'m a function `some_function`')
#     return 10
#
#
# # some_function(1, 2, '3')
# some_function(1, 2, a=3)


# def type_checker(*types):
#
#     def type_checker_wrapper(func):
#
#         def _wrapper(*args, **kwargs):
#             print('Inside `type_checker`')
#             for arg in args:
#                 if not isinstance(arg, types):  # isinstance(arg, (int, float))
#                     raise TypeError
#             for kwarg in kwargs.values():
#                 if not isinstance(kwarg, types):
#                     raise TypeError
#             res = func(*args, **kwargs)
#             return res
#
#         return _wrapper
#
#     return type_checker_wrapper
#
#
# def function_wrapper(func):
#
#     def _wrapper(*args, **kwargs):
#
#         print('Before function')
#         res = func(*args, **kwargs)
#         print('After function')
#
#         return res
#
#     return _wrapper
#
#
# @type_checker(int, float)   # some_function = type_checker(int, float)(some_function)
# def some_function(*args, **kwargs):
#     print('I\'m a function `some_function`')
#     return 10
#
#
# # some_function(1, 1.3)
#
#
# @function_wrapper
# @type_checker(str)  # some_function = function_wrapper(type_checker(int, float)(some_function))
# def some_function2(*args, **kwargs):
#     print('I\'m a function `some_function`')
#     return 10
#
#
# some_function2('1')



"""
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)

"""

# file = open('ex.txt')
#
# for line in file:
#     print(line)
#
# file.close()


with open('ex.txt', 'a') as file:
    file.write('\n')
    file.write('Hello from Python!')
