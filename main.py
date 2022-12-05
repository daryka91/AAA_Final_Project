import enum
import click
from enum import Enum


class Pizza:
    """Parent class"""

    def __init__(self, size: str, ingredients: list[str]):
        # size = ['L', 'XL']
        self.ingredients = ingredients
        self.size = size

    def dict(self):
        print('\n', self.__class__.__name__, sep='\n')
        print('', *self.ingredients, sep='\n-')


class Size(Enum):
    L = 'L'
    XL = 'XL'


class Margherita(Pizza):

    def __init__(self, size: str):
        super().__init__(size, ['tomato sauce', 'mozzarella', 'tomatoes'])
        self.__class__.__name__ += ' 🧀'


class Pepperoni(Pizza):

    def __init__(self, size: str):
        super().__init__(size, ['tomato sauce', 'mozzarella', 'pepperoni'])
        self.__class__.__name__ += ' 🍕'


class Hawaiian(Pizza):

    def __init__(self, size: str):
        super().__init__(size, ['tomato sauce', 'mozzarella', 'chicken',
                                'pineapples'])
        self.__class__.__name__ += ' 🍍'


if __name__ == '__main__':
    a = Margherita('L')
    a.dict()
    b = Pepperoni('XL')
    b.dict()
    c = Hawaiian('L')
    c.dict()
