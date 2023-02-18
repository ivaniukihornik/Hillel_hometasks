import example8

def foo():
    print('in lib')

var2 = int
var3 = '123'

print('123')

foo()

if __name__ == 'lib':
    print('i am lib.py', __name__)