from enum import Enum
from dataclasses import dataclass
import random
from functools import wraps, partial


class Size(Enum):
    """
    Отдельный класс для размера, чтобы не ошибиться при написании и
    иметь возможность легко добавлять новые размеры
    """
    L = 'L'
    XL = 'XL'


def log(func=None, description=None):
    """
    Декоратор, который выводит имя функции и время выполнения, в нашем случае
    это просто случайное число в диапазоне от beg до end.
    Также декоратор может принимать шаблон (description), в который
    подставляет время
    """
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
class Pizza:
    """
    Родительский класс для любой новой пиццы, благодаря тому, что есть
    декоратор @dataclass, автоматически создается метод __eq__ для сравнения
    двух пицц
    """
    size: Size
    ingredients: list[str]

    @classmethod
    def content(cls):
        """
        Метод родительского класса, благодаря которому в меню кафе будут
        автоматически добавляться новые виды пицц при их создании
        """
        for subcls in cls.__subclasses__():
            a = subcls()
            print(f'- {subcls.__name__}{a.emoji}:', sep='', end=' ')
            print(*a.ingredients, sep=', ')

    @log(description='🥘 Приготовили за {} c!')
    @classmethod
    def bake(cls):
        """Выпекаем пиццу"""

    @log(description='🛺 Доставили за {} c!')
    @classmethod
    def delivery(cls):
        """Доставка пиццы"""

    @log
    @classmethod
    def pickup(cls):
        """Самовывоз пиццы"""

    def dict(self) -> None:
        """
        Выводит веселенький рецепт конкретной пиццы
        """
        print('', self.__class__.__name__, self.emoji)
        print('', *self.ingredients, sep='\n-')


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
    b = Pepperoni(Size.XL)
    c = Hawaiian()
    print(b == c)
    Pizza.content()
    Pizza.bake()
    Pizza.delivery()
    Pizza.pickup()
    c.dict()
