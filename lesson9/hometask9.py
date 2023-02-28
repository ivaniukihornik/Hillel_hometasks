# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
# наслідувані від "Транспортний засіб". Наповніть класи атрибутами на свій розсуд.
# Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".
class Vehicle:
    model = None
    owner = 'Ігор'
    owner_age = 43
    owner_rating = 9.87
    sale_status = 'В продажі'


class Car(Vehicle):
    brand = None
    state = None
    color = None
    seats = None
    mileage = None

    def __init__(self, status=None):
        print(f'\nДодайте інформацію про машину власника {self.owner} (вік - {self.owner_age}, рейтинг - '
              f'{self.owner_rating}/10. Введіть:')
        self.brand = input('Бренд - ')
        self.model = input('Модель - ')
        self.state = input('Стан (новий/бу) - ')
        self.color = input('Колір - ')
        self.seats = input('Кількість посадочних місць - ')
        self.mileage = input('Пробіг (тис. км) - ')

        if status is None:
            self.sale_status = 'Продано'


class Ship(Vehicle):
    ship_class = 'Passenger'
    load_capacity = None
    capacity = None
    speed = None
    crew = None

    def __init__(self, status=None):
        print(f'\nДодайте інформацію про корабель власника {self.owner} (вік - {self.owner_age}, рейтинг - '
              f'{self.owner_rating}/10. Введіть:')
        self.model = input('Модель - ')
        self.load_capacity = input('Грузопід\'ємність (т) - ')
        self.capacity = input('Вмістимість (пасажирів) - ')
        self.speed = input('Швидкість (вузлів) - ')
        self.crew = input('Экіпаж - ')

        if status is None:
            self.sale_status = 'Продано'


class Plane(Vehicle):
    plane_class = 'Passenger'
    transportation_type = None
    capacity = None

    def __init__(self, status=None):
        print(f'\nДодайте інформацію про літак власника {self.owner} (вік - {self.owner_age}, рейтинг - '
              f'{self.owner_rating}/10. Введіть:')
        self.model = input('Модель - ')
        self.transportation_type = input('Вид перевозок (міжнародний/регіональний/місцевий)  - ')
        self.capacity = input('Вмістимість (пасажирів) - ')

        if status is None:
            self.sale_status = 'Продано'


car1 = Car('продаю')
ship1 = Ship()
plane1 = Plane('продам')