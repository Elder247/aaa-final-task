import pytest
from PIL.TiffTags import TYPES
from pizza import Margherita, Pepperoni, Hawaiian
from utils import log, delivery, pickup


def test_dict_pizzas():
    """Проверка метода dict() для пицц"""
    expected_margherita = {'tomato sauce': '1 cup',
                           'mozzarella': '7 ounces',
                           'tomatoes': '3'}

    expected_pepperoni = {'tomato sauce': '1 cup',
                          'mozzarella': '7 ounces',
                          'pepperoni': '5'}

    expected_hawaiian = {'tomato sauce': '1 cup',
                         'mozzarella': '7 ounces',
                         'chicken': '10 ounces',
                         'pineapples': '5 ounces'}

    assert Margherita().dict() == expected_margherita
    assert Pepperoni().dict() == expected_pepperoni
    assert Hawaiian().dict() == expected_hawaiian


def test_sizes_pizzas():
    """Проверка значений размера пиццы"""
    assert Margherita('L').size == 'L'
    assert Margherita('XL').size == 'XL'
    with pytest.raises(TypeError):
        Margherita(10)
    with pytest.raises(ValueError):
        Margherita('S')


def test_eq_pizzas():
    """Проверка метода __eq__() для пицц с одинаковыми и разными размерами и ингредиентами"""
    pizza1 = Margherita()
    pizza2 = Margherita('L')
    pizza3 = Margherita('XL')
    pizza4 = Pepperoni()

    assert pizza1 == pizza2
    assert pizza1 != pizza3  # неравенство по размеру
    assert pizza1 != pizza4  # неравенство по ингредиентам


def test_str_pizzas():
    """Проверка метода __str__() для пицц"""
    assert str(Margherita()) == 'Margherita 🍅'
    assert str(Pepperoni()) == 'Pepperoni 🍕'
    assert str(Hawaiian()) == 'Hawaiian 🍍'
