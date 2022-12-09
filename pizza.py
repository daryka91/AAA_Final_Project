import click
import click as cli
from enum import Enum
from dataclasses import dataclass
import random
from functools import wraps, partial


class Size(Enum):
    L = 'L'
    XL = 'XL'


def log(func=None, description=None):
    description_list = []
    if func is None:
        return partial(log, description=description)

    @wraps(func)
    def wrapper(*args, **kwargs):
        beg = 2
        end = 10
        random_order_time = random.randint(beg, end)
        name = func.__name__
        if not description:
            print(f'{name} - {random_order_time}c!')
        else:
            print(description.format(f'{random_order_time}'))

    return wrapper


@dataclass
# Нам не нужно определять методы __eq__, потому что декоратор dataclass
# автоматически добавляет их в определение класса при вызове с order = True
# _DataclassParams(init=True,repr=True,eq=True,order=False,
#                  unsafe_hash=False,frozen=False) - default
class Pizza:
    """Parent class"""
    size: Size
    ingredients: list[str]

    def dict(self) -> None:
        print('', self.__class__.__name__, self.emoji)
        print('', *self.ingredients, sep='\n-')

    @classmethod
    def content(cls):
        for subcls in cls.__subclasses__():
            a = subcls()
            print(f'- {subcls.__name__}{a.emoji}:', sep='', end=' ')
            print(*a.ingredients, sep=', ')

    @log
    @classmethod
    def bake(cls):
        """Выпекаем пиццу"""
        pass

    @log(description='🛺 Доставили за {} c!')
    @classmethod
    def delivery(cls):
        """Доставка пиццы"""
        pass

    @log(description='🏡 Забрали за {} c!')
    @classmethod
    def pickup(cls):
        """Самовывоз пиццы"""
        pass


class Margherita(Pizza):

    def __init__(self, size=Size.L):
        self.emoji = ' 🧀'
        self.ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
        super().__init__(size, self.ingredients)


class Pepperoni(Pizza):

    def __init__(self, size=Size.L):
        self.emoji = ' 🍕'
        self.ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
        super().__init__(size, self.ingredients)


class Hawaiian(Pizza):

    def __init__(self, size=Size.L):
        self.emoji = ' 🍍'
        self.ingredients = ['tomato sauce', 'mozzarella', 'chicken',
                            'pineapples']
        super().__init__(size, self.ingredients)


if __name__ == '__main__':
    b = Pepperoni()
    c = Hawaiian()
    print(b == c)
    Pizza.content()
    Pizza.bake()
    Pizza.delivery()
    Pizza.pickup()
    c.dict()


