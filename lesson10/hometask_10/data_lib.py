# this is just a piece of code to refactor and test
# you have to fix codestyle (I will check it using flake8), write add type-hinting, rename objects if it is necessary
# I will use mypy as well
# you have to fix functions if they work in incorrect way
# write documentation
# remember about namings, especially builtins
# you have to add tests (check errors, types and different values)  and manage its location
# the main idea of this homework - write readable and maintainable code
# function that are called directly here nust be moved to special main file
# it is not a joke - sometimes I receive this kind of code in homeworks
# do not forget about requirements.txt
import string
from random import choice
import random as random_module  # import instruction was moved to the top of the file
# Union method was deleted because it is unused


def get_random_number() -> int:
    """Generate and return int number 'N' in range -10**10 < N < 10**10"""
    number: int = int(random_module.random() * random_module.randint(-10**10, 10**10))
    return number


def random_string_generation(length: int = 10) -> str:
    """Generate a random string of a given length and we never get errors"""
    line: str = ''.join(choice(string.ascii_lowercase) for _ in range(length))
    return line


digit: int = 2
