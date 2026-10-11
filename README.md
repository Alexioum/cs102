# CS102

Лабораторные работы по программированию на Python.
Основа проекта: [шаблон курса](https://github.com/Vl-Tershch/cs-102-template).

## Лабораторная 1. Настройка проекта и окружения

Калькулятор выполняет сложение, вычитание, умножение и деление.
Можно вводить отрицательные и дробные числа. Разделитель дробной части - точка.
После вычисления можно выбрать следующую операцию, для выхода нужно ввести `q`.
Ошибки ввода и деление на ноль не завершают программу.

### Подготовка

Используется Python 3.13. Команды выполняются из корня репозитория:

```bash
python3 -m venv ../.venv
source ../.venv/bin/activate
python -m pip install -r requirements-lab1.txt
```

Файл `requirements.txt` сохранён из шаблона. Для первой работы достаточно
пакетов из `requirements-lab1.txt`.

### Запуск

```bash
python src/lab1/calculator.py
```

### Проверки

```bash
python -m isort --check-only src/lab1/calculator.py
python -m black --check -l 120 src/lab1/calculator.py
python -m mypy src/lab1/calculator.py
python -m pylint src/lab1/calculator.py
python -m pytest -v
```

В тесте из шаблона `assertEquals` заменён на `assertEqual`, поскольку старое
название удалено из Python. Дополнительные тесты проверяют вычисления,
ошибки ввода, повторные операции и выход.

Тесты также выполняются в GitHub Actions при создании pull request.
