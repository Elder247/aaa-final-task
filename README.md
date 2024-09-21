# Pizza Application

## Описание
Приложение для управления заказами пицц через командную строку.
Поддерживаются заказы различных пицц на доставку и самовывоз.

## Установка
1. Склонируйте репозиторий
```bash
git clone https://github.com/Elder247/aaa-final-task.git
```
2. Перейдите в директорию проекта
```bash
cd aaa-final-task
```
3. Установите зависимости
```bash
pip install -r requirements.txt
```

## Использование
### Просмотр меню
```bash
python cli.py menu
```
### Заказ пиццы с самовывозом
```bash
python cli.py order Margherita
```
### Заказ пиццы с доставкой
```bash
python cli.py order pepperoni --delivery
```
### Тестирование
```bash
pytest
```


## Структура
```
pizza-prject
|
|— cli.py
|— pizza.py
|— utils.py
|— test_pizza.py
|— test_cli.py
|— README.md
```
