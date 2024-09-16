from functools import wraps
from random import randint
from typing import Callable
from pizza import Pizza, Margherita, Pepperoni, Hawaiian


def log(pattern: str = '{}c!') -> Callable:
    """
    Декоратор для вывода времени выполнения функции.
    Время подставляется в шаблон pattern вместо символов {}
    """

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
def delivery(pizza_obj: Pizza) -> Pizza:
    """Доставляет пиццу"""
    if not isinstance(pizza_obj, Pizza):
        raise TypeError('Can take only Pizza object')
    return pizza_obj


@log('Забрали за {}с!')
def pickup(pizza_obj: Pizza) -> Pizza:
    """Самовывоз"""
    if not isinstance(pizza_obj, Pizza):
        raise TypeError('Can take only Pizza object')
    return pizza_obj


if __name__ == '__main__':
    f = delivery(Margherita())
    pickup(Pepperoni())
    pickup(Hawaiian())
