#a = 10
#b = 20
#c = a + b
#print(c)

#a1 = 10
#A1 = 20

# print(A2) # comment here

# students_counter = 0  # snake case
# studentsCounter = 0  # camel case

# students_counter = 'abc10'
# res = students_counter + 10

# numbers
# int
my_int1 = 50
my_int2 = 20

#print(type(my_int2))
# res = my_int1 + my_int2
# print(res)
#
# res = my_int1 - my_int2
# print(res)
#
# res = my_int1 * my_int2
# print(res)
#
# res = my_int1 / my_int2
# print(res)
#
# res = my_int1 // my_int2
# print(res)
#
# res = my_int1 ** my_int2
# print(res)
#
# res = my_int1 % my_int2
# print(res)
#
# my_int1 = my_int1 + 10
# my_int1 += 10
# print(res)
#
# # float
#
# res = my_int1 / my_int2
# print(res)
# print(type(res))
#
# my_float = 1.2
# print(my_float)
#
# my_float = 0.0000000000000004 # 16
# print(my_float)
#
# my_float = 4e-17  # 4 * (10** -17)
#
# my_float1 = 0.1
# my_float2 = 0.2
#
# print(my_float1 + my_float2)
# print(my_float1 + my_float2 == 0.3)

# boolean type

# my_float1 = 0.1
# my_float2 = 0.2
#
# my_bool = True
# my_bool = False
#
# print(type(my_bool))
#
# res = my_float1 == my_float2
# print(res)
#
# res = my_float1 > my_float2
# print(res)
#
# res = my_float1 < my_float2
# print(res)
#
# res = my_float1 >= my_float2
# print(res)
#
# res = my_float1 <= my_float2
# print(res)
#
# res = my_float1 != my_float2
# print(res)
#
# # None type
# my_none = None
#
# print(type(my_none))


# str type

# my_str = '324FD#@#$432dsfsds  w 234ds'
# print(type(my_str))
# print(my_str)
#
# my_str = '"some shit"'
# print(my_str)
#
# my_str = "\"some \n shit\""
# print(my_str)
#
# my_str1 = 'abcde'
# my_str2 = '123456'
#
# print(my_str1 + my_str2)
# print(my_str1 * 5)



# data transformation

# my_int = 123
#
# res = float(my_int)
# print(type(res))
# print(res)
#
#
# my_float = 123.923
# res = int(my_float)
# print(res)
# print(type(res))
#
# res = str(my_float)
# print(res)
# print(type(res))
#
#
# # to bool
# print(bool(0))
# print(bool(0.0))
# print(bool(123))
# print(bool(-12421))
# print(bool(' '))
# print(bool(''))
# print(bool(None))



name = 'Ihor'
age = 25

# Hello, my name is Ihor, I`m 25 years old
my_str = 'Hello, my name is ' + name + ', I\'m ' + str(age) + ' years old'  # concatenation
print(my_str)

my_str = 'Hello, my name is %s, I\'m %s years old' % (name, age)
print(my_str)

tpl = 'Hello, my name is %s, I\'m %s years old'
print(tpl % (name, age))

my_str = 'Hello, my name is {}, I\'m {} years old'.format(name, age)
print(my_str)

tpl = 'Hello, my name is {}, I\'m {} years old'
my_str = tpl.format(name, age)
print(my_str)

tpl = 'Hello, my name is {name_value}, I\'m {age_value} years old'
my_str = tpl.format(age_value=age, name_value=name)
print(my_str)

tpl = 'Hello, my name is {1}, I\'m {0} years old'
my_str = tpl.format(age, name)
print(my_str)

my_str = f'Hello, my name is {name}, I\'m {age} years old'
print(my_str)