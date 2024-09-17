from functools import wraps
from random import randint
from typing import Callable
from pizza import Margherita, Pepperoni, Hawaiian


def log(pattern: str = '{}c!') -> Callable:
    """Декоратор для вывода времени выполнения функции. Время подставляется в шаблон pattern вместо символов {}"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            duration = str(randint(1, 5))
            message = pattern.replace('{}', duration)
            print(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('Доставили за {}с!')
def delivery(pizza):
    """Доставляет пиццу"""
    return pizza


@log('Забрали за {}с!')
def pickup(pizza):
    """Самовывоз"""
    return pizza


if __name__ == '__main__':
    delivery(Margherita())
    pickup(Pepperoni())
