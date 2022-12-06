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
# _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False) - default
class Pizza:
    """Parent class"""
    size: Size
    ingredients: list[str]

    def dict(self):
        print('', self.__class__.__name__, sep='\n')
        print('', *self.ingredients, sep='\n-')

    @classmethod
    def content(cls):
        # __name__ встроенное поле любого класса
        # pizzas = [subcls.__name__ for subcls in Pizza.__subclasses__()]
        for subcls in cls.__subclasses__():
            a = subcls(Size.L)
            print(f'{subcls.__name__}: {a.ingredients}')
        # if pizza in Pizza.__subclasses__():
        #     menu.update({pizza.__name__: pizza.ingredients})
        # print(pizzas)


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
#
#
#
# @cli.command()
# def menu():
#     """Выводит меню"""

import inspect



if __name__ == '__main__':
    a = Margherita(Size.L)
    a.dict()
    b = Pepperoni(Size.XL)
    b.dict()
    c = Hawaiian(Size.L)
    c.dict()
    print(b == c)
    # print(Pizza.__subclasses__())
    Pizza.content()

