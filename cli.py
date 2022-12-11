from pizza import Pizza
import click


def pizza_order(pizza: str, delivery: bool):
    Pizza.bake()
    if delivery:
        Pizza.delivery()


@click.group()
def cli():
    pass


@cli.command()
def menu():
    """Выводит меню"""
    Pizza.content()


@cli.command()
@click.option('--delivery', '-d', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу
    Есть пицца трех видов:
    1. pepperoni
    2. margherita
    3. hawaiian
    """
    pizza_order(pizza, delivery)


if __name__ == '__main__':
    cli()
