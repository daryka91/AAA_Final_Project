import click
from enum import Enum
from dataclasses import dataclass


class Size(Enum):
    L = 'L'
    XL = 'XL'


@dataclass
# Нам не нужно определять методы __eq__,
# потому что декоратор dataclass автоматически добавляет их в определение
# класса при вызове с order = True
class Pizza:
    """Parent class"""
    size: Size
    ingredients: list[str]

    def dict(self):
        print('', self.__class__.__name__, sep='\n')
        print('', *self.ingredients, sep='\n-')


class Margherita(Pizza):

    def __init__(self, size: Size):
        self.ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
        super().__init__(size, self.ingredients)
        self.__class__.__name__ += ' 🧀'


class Pepperoni(Pizza):

    def __init__(self, size: Size):
        self.ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']
        super().__init__(size, self.ingredients)
        self.__class__.__name__ += ' 🍕'


class Hawaiian(Pizza):

    def __init__(self, size: Size):
        self.ingredients = ['tomato sauce', 'mozzarella', 'chicken',
                            'pineapples']
        super().__init__(size, self.ingredients)
        self.__class__.__name__ += ' 🍍'


# @click.group()
# def cli():
#     pass
#
#
# @cli.command()
# @click.option(' =delivery', default=False, is_flag=True)
# @click.argument('pizza', nargs=1)
# def order(pizza: str, delivery: bool):
#     """Готовит и доставляет пиццу"""
#     pass
#
# @cli.command()
# def menu():
#     """Выводит меню"""
#     pass

if __name__ == '__main__':
    a = Margherita(Size.L)
    a.dict()
    b = Pepperoni(Size.XL)
    b.dict()
    c = Hawaiian(Size.L)
    c.dict()
    print(b == c)
