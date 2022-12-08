import click
import click as cli
from enum import Enum
from dataclasses import dataclass
import random


class Size(Enum):
    L = 'L'
    XL = 'XL'


def log(function):
    def wrapper(*args, **kwargs):
        beg = 2
        end = 10
        random_order_time = random.randint(beg, end)
        name = function.__name__
        print(f'{name} - {random_order_time}c!')

    return wrapper


@dataclass
# Нам не нужно определять методы __eq__,
# потому что декоратор dataclass автоматически добавляет их в определение
# класса при вызове с order = True
# _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False) - default
class Pizza:
    """Parent class"""
    size: Size
    ingredients: list[str]

    def dict(self):
        print('', self.__class__.__name__, self.emoji)
        print('', *self.ingredients, sep='\n-')

    @classmethod
    def content(cls):
        for subcls in cls.__subclasses__():
            a = subcls(Size)
            print(f'- {subcls.__name__}{a.emoji}:', sep='', end=' ')
            print(*a.ingredients, sep=', ')

    @log
    @classmethod
    def bake(cls):
        pizza = cls
        # pizza: Pizza.__class__
        beg = 1
        end = 10
        random_order_time = random.randint(beg, end)
        print(f'👨‍🍳Приготовили за {random_order_time}c!')

    @classmethod
    def delivery(cls):
        pizza = cls
        beg = 1
        end = 10
        random_order_time = random.randint(beg, end)
        print(f'🎠 Доставили за {random_order_time}c!')


class Margherita(Pizza):

    def __init__(self, size: Size):
        self.emoji = ' 🧀'
        self.ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
        super().__init__(size, self.ingredients)


class Pepperoni(Pizza):

    def __init__(self, size: Size):
        self.emoji = ' 🍕'
        self.ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
        super().__init__(size, self.ingredients)


class Hawaiian(Pizza):

    def __init__(self, size: Size):
        self.emoji = ' 🍍'
        self.ingredients = ['tomato sauce', 'mozzarella', 'chicken',
                            'pineapples']
        super().__init__(size, self.ingredients)


if __name__ == '__main__':
    a = Margherita(Size.L)
    k = Margherita(Size.L)
    b = Pepperoni(Size.L)
    c = Hawaiian(Size.L)
    print(k == a)
    Pizza.content()
    Pizza.bake()
    Pizza.delivery()
