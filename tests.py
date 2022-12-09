import pizza
import cli


def test_pizzaclass():
    piz = pizza.Pizza(pizza.Size.L, ['salmon'])
    test_ingredient = ['salmon']
    assert piz.ingredients == test_ingredient


def test_eq():
    piz1 = pizza.Margherita()
    piz2 = pizza.Margherita()
    assert piz1 == piz2


def test_pizzasize():
    piz = pizza.Margherita()
    test_size = pizza.Size.L
    assert piz.size == test_size


def test_pizzaingredints():
    piz = pizza.Margherita()
    test_ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
    assert piz.ingredients == test_ingredients


def test_pizzaemoji():
    piz = pizza.Margherita()
    test_emoji = ' 🧀'
    assert piz.emoji == test_emoji


def test_pizzacontent(capsys):
    # Capsys-это встроенный модуль, который предоставляет pytest.
    # Это помогает нам фиксировать все, что идет на стандартный
    # вывод и стандартную ошибку во время выполнения теста.
    # Чтобы использовать его, нам нужно включить параметр capsys в
    # список параметров, которые ожидает наша тестовая функция
    piz1 = pizza.Margherita()
    out, err = capsys.readouterr()
    assert '- Margherita 🧀: tomato sauce, mozzarella, tomatoes'


def test_pizzadict(capsys):
    piz = pizza.Margherita()
    out, err = capsys.readouterr()
    assert ' Hawaiian  🍍 -tomato sauce -mozzarella -chicken-pineapples'

def test_menu(capsys):
    piz = pizza.Margherita()
    out, err = capsys.readouterr()
    assert ' Hawaiian  🍍 -tomato sauce -mozzarella -chicken-pineapples'

def test_order(capsys):
    cli.order('pepperoni', False)
    out, err = capsys.readouterr()
    assert