# 1
# Доопрацюйте класс Pоint з заняття наступним чином:
# додайте перевірку координат x та y на числа за допомогою property
class Point:
    x = None
    y = None

    def __init__(self, x_coord, y_coord):
        self.type_checker_x = x_coord
        self.type_checker_y = y_coord

    def type_checker_x_getter(self):
        return self.x

    def type_checker_x_setter(self, value):
        if not type(value) in (int, float):
            raise TypeError

        self.x = value

    type_checker_x = property(type_checker_x_getter, type_checker_x_setter)

    def type_checker_y_getter(self):
        return self.y

    def type_checker_y_setter(self, value):
        if not type(value) in (int, float):
            raise TypeError

        self.y = value

    type_checker_y = property(type_checker_y_getter, type_checker_y_setter)


x1 = 1
y1 = 2
point1 = Point(x1, y1)


# 2
# Доопрацюйте класс Line з заняття наступним чином: додайте можливість порівнювати лінії по довжині
# (==, !=, >=, <=, >, <) за допомогою відповідних методів
class Line:
    line_begin = None
    line_end = None

    def __init__(self, begin_point, end_point):
        self.line_begin = begin_point
        self.line_end = end_point

    def __eq__(self, other):
        are_lines_equal = self.length == other.length
        return are_lines_equal

    def __ne__(self, other):  # !=
        are_lines_not_equal = self.length != other.length
        return are_lines_not_equal

    def __lt__(self, other):  # <
        is_line_smaller = self.length < other.length
        return is_line_smaller

    def __le__(self, other):  # <=
        is_line_equal_or_smaller = self.length <= other.length
        return is_line_equal_or_smaller

    def __gt__(self, other):  # >
        is_line_bigger = self.length > other.length
        return is_line_bigger

    def __ge__(self, other):  # >=
        is_line_equal_or_bigger = self.length >= other.length
        return is_line_equal_or_bigger

    def length_getter(self):
        res = round((((self.line_end.x - self.line_begin.x)**2 + (self.line_end.y - self.line_begin.x)**2)**0.5), 2)
        return res

    length = property(length_getter)


point1_1 = Point(0, 0)
point1_2 = Point(2, 2)
line1 = Line(point1_1, point1_2)

point2_1 = Point(1, 1)
point2_2 = Point(4, 4)
line2 = Line(point2_1, point2_2)

print(f'Length of line 1 - {line1.length}')
print(f'Length of line 2 - {line2.length}')
if line1 == line2:
    print('Line 1 is equal to line 2')

if not line1 == line2:
    print('Line 1 is not equal to line 2')

if line1 >= line2:
    print('Line 1 >= line 2')

if line1 <= line2:
    print('Line 1 <= line 2')

if line1 > line2:
    print('Line 1 > line 2')

if line1 < line2:
    print('Line 1 < line 2')