# Завдання: створити ієрархію класів (реалізувати наслідування) гаджетів (наприклад, телефон та ноутбук зі спільним
# абстрактним предком)
# створити фікстури відповідних сутностей та покрити їх тестами
from abc import abstractmethod, ABC


class Company:
    def __init__(self):
        self.company_name = 'Apple Inc.'
        self.seo = 'Tim Cook'
        self.revenue = 0

    def __str__(self):
        return 'The company {name} headed by {seo} has an income of {revenue}$.'\
            .format(name=self.company_name, seo=self.seo, revenue=self.revenue)

    def update_revenue(self, income: float):
        self.revenue += income
        return self.revenue

    @abstractmethod
    def get_additional_info(self):
        pass


# Створив один підклас. Можна було б додати ще підклас Маків, проте логіка роботи була б однаковою
class Iphone(Company, ABC):
    def __init__(self, model: str, price: float,
                 units_sold: int):
        super().__init__()
        self.model = model
        self.price = price
        self.units_sold = units_sold
        self.total_units_sold = {
            model: units_sold
        }

    def get_income(self) -> float:
        income = self.price * self.units_sold
        self.units_sold = 0  # після передачі прибутку одиниці проданого товара скидуються, щоб не враховувати їх
        # при наступній передачі
        return income

    def update_units_sold(self, amount: int) -> None:
        self.units_sold += amount
        self.total_units_sold[self.model] += amount
