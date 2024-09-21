import pytest
from click.testing import CliRunner
from cli import cli


@pytest.fixture
def runner():
    """Создание экземпляра CliRunner"""
    return CliRunner()


def test_menu_command(runner):
    result = runner.invoke(cli, ['menu'])
    assert result.exit_code == 0
    assert '- Margherita 🍅' in result.output
    assert '- Pepperoni 🍕' in result.output
    assert '- Hawaiian 🍍' in result.output
    assert 'tomato sauce: 1 cup' in result.output


def test_order_no_delivery(runner):
    result = runner.invoke(cli, ['order', 'margherita'])
    assert result.exit_code == 0
    assert 'Приготовили за' in result.output
    assert 'Забрали самостоятельно за' in result.output


def test_order_with_delivery(runner):
    result = runner.invoke(cli, ['order', 'hawaiian', '--delivery'])
    assert result.exit_code == 0
    assert 'Приготовили за' in result.output
    assert 'Доставили за' in result.output
