# functions

# DRY

# def function_name(arg1, arg2):
#     print('inside function 1', arg1)
#     print('inside function 2', arg2)
#     print('inside function 3')
#
#
# function_name(1, 'arg') # positional (позиционная передача аргументов)
# function_name(2, 'arg')
#
# function_name(arg2='abcde', arg1=12) # named


# def function_name(arg1, arg2, arg3):
#     print('inside function 1', arg1, arg2, arg3)
#     print(type(arg1), type(arg2), type(arg3))
#
#
# function_name(10, 'arg2', arg3=None) # позиционные элементы передаются ТОЛЬКО ВНАЧАЛЕ
#
#
# def function_name(arg1, arg2, arg3):
#     print('inside function 1', arg1, arg2, arg3)
#     print(type(arg1), type(arg2), type(arg3))
#     res = arg1 + arg2 + arg3
#     return res
#
# result = function_name(1, 2, 3)
# print(result)
# print(type(result))
#
#
# def div(value, divisor=1):
#     print('inside')
#     print(f'{value} / {divisor}')
#     return value / divisor
#
# res = div(10,)
# print(res)
#
#
# def list_updater(data_to_add, list_to_update=[]):  # list_to_update создается в момент создани функции
#
#     list_to_update.append(data_to_add)
#
#     return list_to_update
#
# my_list = [1, 2, 3]
#
# my_list = list_updater(4, my_list)
# print(my_list)
#
# new_list = list_updater(10)
# print(new_list)
#
# my_list = list_updater(5, my_list)
# print(my_list)
#
# new_list = list_updater(20)
# print(new_list)
#
# new_list = list_updater(30)
# print(new_list)


# def list_updater(data_to_add, list_to_update=None):
#
#     if list_to_update is None:
#         list_to_update = []
#
#     list_to_update.append(data_to_add)
#     return list_to_update
#
# my_list = [1, 2, 3]
#
# my_list = list_updater(4, my_list)
# print(my_list)
#
# new_list = list_updater(10)
# print(new_list)
#
# my_list = list_updater(5, my_list)
# print(my_list)
#
# new_list = list_updater(20)
# print(new_list)
#
# new_list = list_updater(30)
# print(new_list)

# def list_updater(data_to_add, list_to_update=None):
#     print(f'inside list id is: {id(list_to_update)}')
#     if list_to_update is None:
#         list_to_update = []
#
#     list_to_update.append(data_to_add)
#
#     return list_to_update
#
# my_list = [1, 2, 3]
# print(id(my_list))
# print(my_list)
#
# my_list = list_updater(4, my_list)
# print(my_list)
#
# my_list = list_updater(5, my_list)
# print(my_list)


# def my_function(arg1, arg2, arg3, *args):
#     print('Inside function')
#     print('arg1:', arg1)
#     print('arg2:', arg2)
#     print('arg3:', arg3)
#
#     print('args', args)
#     print('args', type(args))
#
# my_function(1, 2, 3, 4, 5)
# my_function(1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# my_arg_list = [1, 2, 3, 4, 5, 6, 7]
# my_function(*my_arg_list)

# def my_function(arg1, arg2, arg3, *args):
#     print('Inside function')
#     print('arg1:', arg1)
#     print('arg2:', arg2)
#     print('arg3:', arg3)
#
# my_function(arg1=10, arg2=20, arg3=30)
#
# data_dict = {
#     'arg1': 10,
#     'arg2': 20,
#     'arg3': 30
# }
#
# my_function(**data_dict)  # my_function(arg1=10, arg2=20, arg3=30)

# def my_function(**kwargs):  # не может принимать позиционные аргументы
#     print('inside func')
#     print('kwargs:', kwargs)
#
# my_function(arg1=10, arg2=20, arg3=30, a=10, b=20)
#
# data_dict = {
#     'arg1': 10,
#     'arg2': 20,
#     'arg3': 30
# }
#
# my_function(**data_dict)  # my_function(arg1=10, arg2=20, arg3=30)


# def my_function(*args):  # не может принимать именованные элементы

def my_function(*ars, **kwargs):
    print()