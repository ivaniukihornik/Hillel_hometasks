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


# import math
#
#
# class Points(object):
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __sub__(self, no):
#         x = self.x - no.x
#         y = self.y - no.y
#         z = self.z - no.z
#         return Points(x, y, z)
#
#     def dot(self, no):
#         x = self.x * no.x
#         y = self.y * no.y
#         z = self.z * no.z
#         return x + y + z
#
#     def cross(self, no):
#         x = self.y * no.z - self.z * no.y
#         y = self.z * no.x - self.x * no.z
#         z = self.x * no.y - self.y * no.x
#         return Points(x, y, z)
#
#     def absolute(self):
#         return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
#
#
# if __name__ == '__main__':
#     points = list()
#     for i in range(4):
#         a = list(map(float, input().split()))
#         points.append(a)
#
#     P_a = [0, 4, 5]
#     P_b = [1, 7, 6]
#     P_c = [0, 5, 9]
#     P_d = [1, 7, 2]
#
#     a, b, c, d = Points(*P_a), Points(*P_b), Points(*P_c), Points(*P_d)
#     x = (b - a).cross(c - b)
#     y = (c - b).cross(d - c)
#     angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
#
#     print("%.2f" % math.degrees(angle))


# import operator
#
#
# def person_lister(f):
#     def inner(people):
#         people_new = []
#         for body in people:
#             body_new = []
#             for index, data in enumerate(body):
#                 if index == 2:
#                     body_new.append(int(data))
#                 else:
#                     body_new.append(data)
#             people_new.append(body_new)
#
#         people_new.sort(key=operator.itemgetter(2))
#         print('people new', *people_new, sep='\n')
#         res = []
#         for body in people_new:
#             res.append(f(body))
#         return res
#
#     return inner
#
#
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
#
#
# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')


# import operator
#
#
# def person_lister(f):
#     def inner(people):
#         # complete the function
#         data = sorted(people, key=lambda person: int(person[2]))
#         sorted_people = []
#         for person in data:
#             sorted_people.append(f(person))
#         return sorted_people
#
#     return inner
#
#
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[
#         1]
#
#
# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')
# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver
#
# class Button:
#     def __init__(self, driver):
#         self.driver: WebDriver = driver
#         self.URL = 'https://demoqa.com/radio-button'
#         self.button_locator = 'label[for=\'{}Radio\']'
#         self.button_status_locator = 'input#{}Radio'
#         self.buttons_locator = 'label[for*=\'Radio\']'
#
#     def open_page(self):
#         self.driver.get(self.URL)
#
#     def get_buttons_info(self):
#         buttons = []
#         for el in self.driver.find_elements(By.CSS_SELECTOR, self.buttons_locator):
#             buttons.append(el.text)
#         return buttons
#
#
# @pytest.mark.usefixtures('chrome')
# class Test:
#     def test(self):
#         abc = Button(self.driver)
#         abc.open_page()
#         result = abc.get_buttons_info()
#         print(result)


name = 'John'
age = 24
string = f'My name is {name}. I am {age}'
print(string)

a = 'bbabb'
print(a*2)