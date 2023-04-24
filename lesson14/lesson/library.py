import hashlib

from abc import ABC, abstractmethod


class Owner(ABC):
    def __init__(self, name: str, inn: str, address: str, is_legal: bool = False):
        self.name = name.upper()
        self.inn = inn
        self.address = address
        self.is_legal = is_legal

    def __str__(self):
        return f'{self.name}: {self.inn} registered {self.address}'

    @abstractmethod
    def get_additional_info(self):
        pass


class Company(Owner):
    def __init__(self, name: str, inn: str, address: str, balance: int):
        self.is_legal = True
        super().__init__(name=name, inn=inn, address=address, is_legal=self.is_legal)
        self.rating = None
        self.balance = balance

    def get_additional_info(self):
        return f'Current balance: {self.balance}'

    @property
    def get_company_rating(self):
        if self.balance > 100_000:
            self.rating = 'A'
            return self.rating
        else:
            self.rating = 'B'
            return self.rating


# apple = Company('Apple', '0012345', 'Kyiv', 313231)
# print(apple)


class Person(Owner):
    def __init__(self, name: str, inn: str, address: str, has_stable_work: bool = True, is_legal: bool = False):
        super().__init__(name=name, inn=inn, address=address, is_legal=is_legal)
        self.has_stable_work = has_stable_work

    def get_additional_info(self):
        return f'Has stable work: {self.has_stable_work}'


class Account:
    def __init__(self, client: Owner, secret_word: str):
        self.client = client
        self.rate = 10 if self.client.is_legal else 20
        self.__password = Account.__encryption(secret_word)
        print(self.__password)
        if self.client.is_legal:
            self.client.balance += 1000

    def get_some_info(self, secret_word):
        if Account.__encryption(secret_word) == self.__password:
            return 'some info'
        else:
            return 'reject'

    @staticmethod
    def __encryption(word: str):
        encrypted_result = hashlib.md5(word.encode()).hexdigest()
        print(encrypted_result)
        return encrypted_result

# company_data = Company(
#         name='Apple',
#         inn='0006547654',
#         address='Kyiv',
#         balance=100_000,
#     )
#
# account = Account(company_data, '1236565656555655555556')
#
# print(account.get_some_info('123'))

