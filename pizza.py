from abc import ABC, abstractmethod
from functools import total_ordering


@total_ordering
class Pizza(ABC):
    def __init__(self):
        ingredients = ['tomato sauce', 'mozzarella']
        size = None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.size == other.size
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            if self.size == 'L' and other.size == 'XL':
                return True
            return False
        return NotImplemented



class Margherita(Pizza):
    def __init__(self):
        symbol = u'\U0001F345'

class Pepperoni(Pizza):
    def __init__(self):
        symbol = u'\U0001F355'


class Hawaiian(Pizza):
    def __init__(self):
        symbol = u'\U0001F34D'










