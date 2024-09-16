from abc import ABC
from typing import Dict, Any


class Pizza(ABC):
    def __init__(self, size_value: str = 'L') -> None:
        self.size = size_value
        self.ingredients: Dict[str, str] = {}
        self.symbol: str = ''

    @property
    def size(self) -> str:
        return self._size

    @size.setter
    def size(self, value: Any) -> None:
        if not isinstance(value, str):
            raise TypeError('Only string type available')
        if value not in ('L', 'XL'):
            raise ValueError('Only L and XL sizes for pizza available')
        self._size = value

    def dict(self) -> Dict[str, str]:
        """Выводит рецепт пиццы в виде словаря dict"""
        print(self.ingredients)
        return self.ingredients

    def __eq__(self, other: object) -> bool:
        """Проверяет равенство пицц по размеру и ингредиентам"""
        if isinstance(other, Pizza):
            return (
                    self.size == other.size and
                    self.ingredients == other.ingredients
            )
        return NotImplemented

    def __str__(self) -> str:
        """Возвращает строковое представление в виде 'Название Символ'"""
        return f'{self.__class__.__name__} {self.symbol}'


class Margherita(Pizza):
    def __init__(self, size: str = 'L') -> None:
        super().__init__(size)
        self.symbol = u'\U0001F345'  # 🍅
        self.ingredients = {'tomato sauce': '1 cup',
                            'mozzarella': '7 ounces',
                            'tomatoes': '3'}


class Pepperoni(Pizza):
    def __init__(self, size: str = 'L') -> None:
        super().__init__(size)
        self.symbol = u'\U0001F355'  # 🍕
        self.ingredients = {'tomato sauce': '1 cup',
                            'mozzarella': '7 ounces',
                            'pepperoni': '5'}


class Hawaiian(Pizza):
    def __init__(self, size: str = 'L') -> None:
        super().__init__(size)
        self.symbol = u'\U0001F34D'  # 🍍
        self.ingredients = {'tomato sauce': '1 cup',
                            'mozzarella': '7 ounces',
                            'chicken': '10 ounces',
                            'pineapples': '5 ounces'}


if __name__ == '__main__':
    margherita = Margherita('XL')
    pepperoni = Pepperoni()
    print(margherita)
    print(pepperoni)
