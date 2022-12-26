import pizza
from cli import order, menu
from click.testing import CliRunner


def test_pizza_class():
    piz = pizza.Pizza(pizza.Size.L, ['salmon'])
    test_ingredient = ['salmon']
    assert piz.ingredients == test_ingredient


def test_eq():
    piz1 = pizza.Margherita()
    piz2 = pizza.Margherita()
    assert piz1 == piz2


def test_pizza_size():
    piz = pizza.Margherita()
    test_size = pizza.Size.L
    assert piz.size == test_size


def test_pizza_ingredients():
    piz = pizza.Margherita()
    test_ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']
    assert piz.ingredients == test_ingredients


def test_pizza_emoji():
    piz = pizza.Margherita()
    test_emoji = ' 🧀'
    assert piz.emoji == test_emoji


def test_pizza_content(capsys):
    # Capsys-это встроенный модуль, который предоставляет pytest.
    # Это помогает нам фиксировать все, что идет на стандартный
    # вывод и стандартную ошибку во время выполнения теста.
    # Чтобы использовать его, нам нужно включить параметр capsys в
    # список параметров, которые ожидает наша тестовая функция
    pizza.Pizza.content()
    out, err = capsys.readouterr()
    assert '- Margherita 🧀: tomato sauce, mozzarella, tomatoes' in out


def test_pizza_dict(capsys):
    piz = pizza.Hawaiian()
    piz.dict()
    out, err = capsys.readouterr()
    assert ' Hawaiian  🍍 -tomato sauce -mozzarella -chicken -pineapples'


def test_pickup(capsys):
    pizza.Pizza.pickup()
    out, err = capsys.readouterr()
    assert 'pickup -' in out


def test_click_order_delivery():
    runner = CliRunner()
    result = runner.invoke(order, ['pepperoni', '-d'])
    assert '🥘 Приготовили за' in result.output
    assert '🛺 Доставили за' in result.output


def test_click_order():
    runner = CliRunner()
    result = runner.invoke(order, ['pepperoni'])
    assert '🥘 Приготовили за' in result.output


def test_click_menu():
    runner = CliRunner()
    result = runner.invoke(menu)
    assert '- Margherita 🧀: tomato sauce, mozzarella, tomatoes' in result.output
