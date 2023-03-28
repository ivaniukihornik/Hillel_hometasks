# import re
# text = ''' The Hubble.Space.Telescope (often referred to as HST or Hubble) is a space telescope that was launched into low Earth orbit in 1990 and remains in operation.... It was not the first space telescope, but it is one of the largest and most versatile, renowned both as a vital research tool and as a public relations boon for astronomy. The Hubble telescope is named after astronomer Edwin Hubble and is one of NASA's Great Observatories..... The Space Telescope Science Institute (STScI) selects Hubble's targets and processes the resulting data, while the Goddard Space Flight Center (GSFC) controls the spacecraft.A commission headed by Lew Allen, director of the Jet Propulsion Laboratory, was established to determine how the error could have arisen. The Allen Commission found that a reflective null corrector, a testing device used to achieve a properly shaped non-spherical mirror, had been incorrectly assembled—one lens was out of position by 1.3 mm (0.051 in).'''
# split_regex = re.compile(r'(?<=[.|?|!|…])\s+')
#
# sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(text)])
# for s in sentences:
#     print(s)

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
# wrapped_function = function_wrapper(some_function)
#
# some_function()
# wrapped_function()


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
# @type_checker(str)  # some_function = function_wrapper(type_checker(str)(some_function))
# def some_function2(*args, **kwargs):
#     print('I\'m a function `some_function`')
#     return 10
#
#
# some_function2('2')


from collections import defaultdict


li = ['a', 'b', 'c']
B = defaultdict(list)

A = ['a', 'a', 'b', 'a', 'b']


for k, v in enumerate(A):
    B[v].append(k+1)


m = 2
for i in range(m):
    print(' '.join(str(index) for index in (B.get('a', [-1]))))
