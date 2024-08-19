<h2>Автотесты на API проекта «Битва покемонов»</h2>

> **Статус проекта:**
> Проект закрытый для POST запросов, но GET можно выполнять без токена: https://pokemonbattle.ru/
> 
> 🟢 Поддерживается (активный) 

## Описание проекта и задачи
Автоматизировать часть проверок регресса с помощью Pytest и Requests

## Скрипт - `main.py`
* Создание покемона `POST /pokemons`
* Смена имени покемона `PUT /pokemons`
* Поймать покемона в покебол `POST /trainers/add_pokeball`

## Тест-кейсы, которые автоматизировали - `tests/test_pokemon.py`
* Получение списка тренеров и проверка кода ответа `GET /trainers`
* Получение имени моего тренера `GET /trainers` с указанием квери-параметра `trainer_id` и проверка имени на соответствие
* Получение моего тренера `GET /trainers` с указанием квери-параметра `trainer_id` и проверка всех аатрибутов на соответствие

Ожидаемый ответ: 
* response `status code` = 200
* в ответе в `json` приходит корректное поле `trainer_name`
* в ответе приходят корректные поля `id`, `trainer_name`, `level`, `get_history_battle`, `is_premium`, `premium_duration`, `city` в json

## Детали реализации

1. Автотесты написаны с применением PyTest
2. Используется библиотека Requests
3. Параметризированный автотест с использованием декоратора

![image](https://raw.githubusercontent.com/thunderom/python_pytest_and_requests/main/img/decorator.png)

## Локальный запуск тестов (из терминала)
1. Скачать проект
2. Вставить в `main.py` своё значение `TOKEN`
3. Вставить в `test_pokemons.py` свои значения `TOKEN`, `TRAINER_ID` и `TRAINER_NAME`
4. Перейти через терминал в директорию проекта
5. Выполнить команды:

Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```

6. Устанавливаем библиотеки

``` markdown
python3 -m pip3 install requests
```

``` markdown
python3 -m pip3 install pytest
```

7. Запускаем
``` markdown
python3 main.py
pytest tests/test_pokemon.py
```

## Ожидаемый результат
Получаем отчет о прохождении тестов.

## Автор

 Роман Гранд ([@r_grand](https://t.me/r_grand))