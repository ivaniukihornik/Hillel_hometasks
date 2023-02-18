# import random
#
# print(dir())
#
# print(random.randint(1, 10))

# from random import randint
#
# print(randint(1, 10))

# import random  # чтобы модуль не перезаписывался например переменной, его можно переназывать
#
# random = 10


# import random as RANDOM
#
# print(dir())
# print(RANDOM.randint(1, 10))
#
#
# from random import randint as RI
#
# print(RI(1, 100))


# import random, os
# #
# import random  # better to import each module separately
# import os


# from random import random  # with renamed functions to another line
# from random import randint as RI, choice as CHOICE
#
# from random import (
#     randint as RI,
#     choice as CHOICE
# )


# from random import *  # random, randint ... в этом случае все функции импортируются через запятую вместо подгрузки всего модуля


# import lib
#
# lib.var2
# lib.foo()
#
# from lib import foo as FOO

# import lib  # python3 lib.py

# print('i am example.py', __name__)
#
# def foo():
#     print('Foo')




# file = open('requirements.txt', 'r')
#
# for line in file:
#     print(line)
#
# file.close



with open('requirements.txt', 'a') as file:
    file.write('\nHello from example8')