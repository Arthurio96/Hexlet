**Симулятор распределённой системы**

Этот проект представляет симуляцию распределённой системы для выполнения заданий на нескольких серверах. Программа демонстрирует работу с очередями и алгоритмами распределения задач с учётом приоритетов.

**Функциональность**

Инициализация системы:
- Пользователь задаёт количество серверов.
- Каждый сервер может выполнять только одно задание одновременно.

Добавление заданий:
- Задания имеют время выполнения и приоритет.
- Задания направляются на сервер с минимальной загрузкой.
- Если все серверы заняты, задание добавляется в очередь.

Обработка заданий:
- Задания на серверах обрабатываются по тикам.
- Завершённые задания удаляются, и серверы берут следующие задания из очереди.

Очередь с приоритетом:
- Задания в очереди сортируются по приоритету (от большего к меньшему).

Просмотр состояния:
- Вывод состояния серверов (текущее задание, оставшееся время выполнения).
- Вывод содержимого очереди.

**Команды**

`добавить <время> <приоритет>` — добавляет задание с указанным временем выполнения и приоритетом.

`тик` — симулирует один шаг времени.

`статус` — отображает текущее состояние серверов и очереди.

`выход` — завершает выполнение программы.

**Пример работы**

## Пример работы
```
Добро пожаловать в симулятор распределенной системы.
Введите количество серверов: 2
Команда (добавить <время> <приоритет>, тик, статус, выход): добавить 5 10
Задание с 5 секундами выполнения и приоритетом 10 направлено на Сервер 1.
Команда (добавить <время> <приоритет>, тик, статус, выход): добавить 3 20
Задание с 3 секундами выполнения и приоритетом 20 направлено на Сервер 2.
Команда (добавить <время> <приоритет>, тик, статус, выход): добавить 7 5
Задание с 7 секундами выполнения и приоритетом 5 добавлено в очередь.
Команда (добавить <время> <приоритет>, тик, статус, выход): тик
Команда (добавить <время> <приоритет>, тик, статус, выход): статус
Сервер 1: выполняет задание с приоритетом 10 (осталось 4 сек.)
Сервер 2: выполняет задание с приоритетом 20 (осталось 2 сек.)
Очередь заданий: [(7, 5)]
```
## Требования

**Требования**

Python 3.8+

Совместимость с любым терминалом.

**Запуск**

- Скачайте файл distributed_system.py.
- Выполните команду ```python python3 distributed_system.py
- Следуйте инструкциям в консоли.

**Лицензия**

MIT License.
