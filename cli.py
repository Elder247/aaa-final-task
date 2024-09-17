import click
from pizza import Margherita, Pepperoni, Hawaiian


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True, help='Передает пиццу с курьером')
@click.argument('pizza')
def order(pizza: str, delivery: bool) -> None:
    """Готовит и доставляет пиццу"""
    if pizza.lower() not in ('margherita', 'pepperoni', 'hawaiian'):
        click.echo('Данная пицца отсутствует в меню')
        return

    click.echo(f'Приготовили за 2с!')
    if delivery:
        click.echo(f'Доставили за 1с!')
    else:
        click.echo(f'Забрали самостоятельно за 1с!')


@cli.command()
def menu() -> None:
    """Выводит меню"""
    for pizza in (Margherita(), Pepperoni(), Hawaiian()):
        ingredients_string = ', '.join(f'{key}: {value}' for key, value in pizza.ingredients.items())
        click.echo(f'- {pizza}: {ingredients_string}')


if __name__ == '__main__':
    cli()
