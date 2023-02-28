# # OOP principles
#
# # Abstraction
# # Encapsulation
# # Inheritance
# # Polymorphism
#
#
# class MyClassName:
#     pass
#
#
# my_obj = MyClassName()
#
# print(my_obj)
# print(type(my_obj))


# class User:
#     name = 'Artem'
#     age = 39
#
#     def say_hello(self):
#         return f'Hello, my name is {self.name}, i\'m {self.age} years old'
#
#
# user1 = User()
#
# print(user1.name)
# print(user1.age)
#
# print(user1.say_hello())  # User.say_hello(user1)
# # print(User.say_hello(user1))
#
# user1.name = 'Oleg'
#
# print(user1.say_hello())


# class User:
#     name = 'Artem'
#     age = 39
#
#     def say_hello(self, prefix='Hi'):
#         return f'{prefix}, my name is {self.name}, i\'m {self.age} years old'
#
#
# user1 = User()
# print(user1.name)
# print(user1.say_hello())
#
# user2 = User()
# user2.name = 'Bogdan'
#
# print(user2.name)
# print(user2.say_hello('Hello'))

# user2.address = '12345678zxbnm,'
# print(user2.address)

# var = 'address'
# # user2.var
#
# res = hasattr(user2, var)
# print(res)
#
# res = getattr(user2, var, None)
# print(res)
#
# setattr(user2, var, '12345678zxbnm,')
#
# res = getattr(user2, var, None)
# print(res)
#
# delattr(user2, var)
#
# res = getattr(user2, var, None)
# print(res)


# class User:
#     name = 'Artem'
#     age = 39
#
#     _phone = '123456789'  # protected
#
#     __address = 'hsbdfbegvhpro'  # private
#
#     def say_hello(self, prefix='Hi'):
#         msg = f'''
#         {prefix}, my name is {self.name}, i\'m {self.age} years old.
#         My phone is {self._phone}.
#         My address is {self.__address}.
#         '''
#         self.__bar()
#         return msg
#
#     def _foo(self, ):
#         print('In _foo')
#
#     def __bar(self, ):
#         print('In __bar')
#
#
# user1 = User()
# print(user1.name)
# print(user1.say_hello())
# print(user1._phone)
# # print(user1.__address)
#
# print(user1._User__address)
# print(user1._foo())
# # print(user1.__bar())


# class User(object):  # 2.x
# class User:  # 3.x
#     name = 'Artem'
#     age = 39
#
#     def say_hello(self, prefix='Hi'):
#         msg = f'''{prefix}, my name is {self.name}, i\'m {self.age} years old.'''
#         return msg
#
#
# class Programmer(User):
#     language = 'Python'
#
#     def say_hello(self, prefix='Hi'):
#         msg = f'''{prefix}, my name is {self.name}, i\'m {self.age} years old. I\'m a {self.language} programmer.'''
#         return msg
#
#
# user1 = User()
# print(dir(user1))
#
# # print(user1.name)
# # # print(user1.language)
# # # print(user1.say_hello())
# #
# # programmer1 = Programmer()
# # print(programmer1.name)
# # print(programmer1.language)
# # print(programmer1.say_hello())
# #
# # # MRO
# #
# # print(type(user1))
# # print(type(programmer1))
# #
# # print(isinstance(programmer1, Programmer))
# # print(isinstance(programmer1, User))


class User:
    name = 'Artem'
    age = 39
    address = 'sdfghjkl'

    def __init__(self, new_name, new_age=None):
        print('In __init__', self.name)
        print('In __init__', self.age)
        self.name = new_name

        if new_age is not None:
            self.age = new_age

        self.say_hello()

    def say_hello(self, prefix='Hi'):
        msg = f'''{prefix}, my name is {self.name}, i\'m {self.age} years old.'''
        print(msg)
        return msg


user1 = User('Anton')

print(user1.name)
print(user1.address)
# print(user1.say_hello())
