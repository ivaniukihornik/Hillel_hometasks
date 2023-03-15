a = 'student 1 2 3'
b = 'first second third'
c = {}

v, *marks = a.split()
score = list(map(int, marks))
print(marks)


def test():
    assert 10 == 10
