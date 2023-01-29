# repeat data types
# repeat string

my_str = "qwe"
my_str = 'qwe'
my_str_few_rows = '''qwe
qwe
qwe'''

# string methods

print(my_str_few_rows)
print('abc' in my_str)
print('w' in my_str)
print(len(my_str_few_rows))

my_str = 'abc {} 123'
result = my_str.format('HERE', '2')
print(result)

my_str = 'abc 123 abc'
result = my_str.replace('ab', '&&&')
print(result)


my_str = '----abc 1---23 abc---'
result = my_str.strip('-') # замена нужных символов в начале и в конце строки
print(result)

my_str = '----abc 1---23 abc---'
result = my_str.lstrip('-')
print(result)

my_str = '----abc 1---23 abc---'
result = my_str.rstrip('-')
print(result)

my_str = '----aBc 1---23 aBC---'
result = my_str.upper()
print(result)

my_str = '----aBc 1---23 aBC---'
result = my_str.lower()
print(result)

my_str = 'abc AbsewSDesWWdG'
result = my_str.title()
print(result)

my_str = 'abc AbsewSDesWWdG'
result = my_str.count('ab')
print(result)

my_str = 'abc AbsewSDesWWdG'
result = my_str.startswith('ab') # начинается ли стринг с нужных символов
print(result)

my_str = 'abc AbsewSDesWWdG'
result = my_str.endswith('ab')
print(result)

my_str = '123'
result = my_str.isdigit()
print(result)

my_str = '123'
result = my_str.isalpha() # состоит ли строка только из букв
print(result)

my_str = '123'
result = my_str.isalnum() # состоит ли строка только из букв и цифр
print(result)


# input

# result = input('Insert some data here ') # останавливает работу интерпретатора, принимает данные с клавиатуры и останавливается после нажатия "Ентер"
# print(f'input result is ----> {result}')

my_str = 'ab  cdefgh'
result = my_str.find('cd')
print(result)

my_str = '0123456789'
print(my_str[0])
print(my_str[2].isnumeric())

# my_str[1] = '2' #заменить данные в стринге через обращение по индексу элемента нельзя

print(my_str[len(my_str)-1])
print(my_str[-1])
print(my_str[2:5]) # слайс - строка обрезается перед элементами 2 и 5
print(my_str[2:55555])
print(my_str[:5]) # my_str[0:5]
print(my_str[-1:]) # my_str[-1]
print(my_str[-5:-2])

print(my_str[2:7:2]) # выборка с шагом
print(my_str[2::2])
print(my_str[-2:-7:-2])

print(my_str[len(my_str) // 2:])

avg_index = len(my_str) // 2
print(my_str[avg_index:])

print(my_str[:len(my_str) // 2])

print(my_str[:])
print(my_str[::-1]) # развернуть стринг задом наперед



# if/else

condition = True

if condition:
    print('It\'s true '*4)
else:
    print('false')


condition = 10

if condition:
    print('It\'s true '*4)
else:
    print('false')


var_a = 10
var_b = 20


if var_a > var_b:
    print('It\'s true '*4)
else:
    print('false')


# elif

if var_a > var_b:
    print('var_a > var_b')
elif var_a == var_b:
    print('var_a == var_b')
elif var_a < var_b:
    print('var_a < var_b')


# git
