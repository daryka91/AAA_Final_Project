import click as cli
from enum import Enum
from dataclasses import dataclass


class Size(Enum):
    L = 'L'
    XL = 'XL'

class Emoji(Enum):
    marg = ' 🧀'
    peper = ' 🍕'
    haw = ' 🍍'


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
            a = subcls(Size.L)
            print(f'- {subcls.__name__}{a.emoji}:', sep='', end=' ')
            print(*a.ingredients, sep=', ')


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
@cli.command()
def menu():
    """Выводит меню"""
    Pizza.content()


if __name__ == '__main__':

    a = Margherita(Size.L)
    k = Margherita(Size.L)
    b = Pepperoni(Size.L)
    c = Hawaiian(Size.L)
    a.dict()
    print(k == a)
    # print(Pizza.__subclasses__())
    # Pizza.content()
    menu()

