import pytest
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


def test_eq_pizzas():
    pizza1 = Margherita()
    pizza2 = Margherita('L')
    pizza3 = Margherita('XL')
    pizza4 = Margherita('S')
