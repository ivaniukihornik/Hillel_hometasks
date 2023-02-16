# def my_function(arg1, arg2):
#     print(arg1, arg2)
#     result = arg1 + arg2
#     return result
#
#
#
#
# def my_next_function(arg1, arg2):
#     print(arg1, arg2)
#     result = my_function(arg1, arg2)
#     return result
#
# my_next_function(10, 20)



global_value = 100


print(dir())

def bar():
    foo(10, 20)
    pass

def foo(arg1, arg2):
    local_value = 200
    global_value = 200
    print(global_value)
    print(dir())

print('be')
foo(1, 2)