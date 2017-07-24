# Данные о курсах на Курсере

Cобирает информацию о разных курсах на Курсере, приводит её в удобный для обработки вид и выгружает в эксель-файл.

# Установка и использование

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 и библиотек BeautifulSoup4, requests, openpyxl, lxml

Установка библиотек:

```#!bash
pip install -r requirements.txt
```

Справка:

```
usage: coursera.py [-h] [-q QUANTITY] output

positional arguments:
  output                xlsx-файл в который будут выгружены данные

optional arguments:
  -h, --help            show this help message and exit
  -q QUANTITY, --quantity QUANTITY
                        Колличество спарсеных курсов. Изначально – 20
```

Пример использования:
`$ python3 coursera.py output.xlsx -q 5`

[Пример файла на выходе](https://docs.google.com/spreadsheets/d/1cah29Eaw04mljasXTAIPdV9avJrmsgz7No4OiNb3tFM/edit?usp=sharing)
# Цель проекта

Это код написан в образовательных целях. Тренировачный курс для веб-девелоперов - [DEVMAN.org](https://devman.org)
