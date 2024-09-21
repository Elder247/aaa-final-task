import click
from pizza import ALL_PIZZAS


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--delivery',
              default=False,
              is_flag=True,
              help='Передает пиццу с курьером')
@click.argument('pizza')
def order(pizza: str, delivery: bool) -> None:
    """Готовит и доставляет пиццу"""
    if pizza.lower() not in ('margherita', 'pepperoni', 'hawaiian'):
        click.echo('Данная пицца отсутствует в меню')
        return

    click.echo('Приготовили за 2с!')
    if delivery:
        click.echo('Доставили за 1с!')
    else:
        click.echo('Забрали самостоятельно за 1с!')


@cli.command()
def menu() -> None:
    """Выводит меню"""
    for PizzaClass in ALL_PIZZAS:
        pizza = PizzaClass()
        ingredients_string = ', '.join(
            f'{key}: {value}' for key, value in pizza.ingredients.items()
        )
        click.echo(f'- {pizza}: {ingredients_string}')


if __name__ == '__main__':
    cli()
