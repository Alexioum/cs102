# Лабораторная 2. Алгоритмы шифрования

Реализованы шифры Цезаря и Виженера, проверка простоты числа,
алгоритм Евклида, поиск обратного числа и генерация ключей RSA.

Файлы находятся в `src/lab2`. Название `vigenre.py` сохранено из шаблона курса.
Готовый код, комментарии и примеры из шаблона сохранены.

## Запуск

Для самих алгоритмов достаточно Python, дополнительные библиотеки не нужны.
Команды выполняются из корня репозитория:

```bash
python3 -m venv ../.venv
source ../.venv/bin/activate
python -m pip install -r requirements-lab2.txt
```

Если окружение уже создано для первой работы, достаточно его активировать.

Примеры вызовов в Python:

```python
from src.lab2.caesar import encrypt_caesar, decrypt_caesar
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere
from src.lab2.rsa import generate_keypair, encrypt, decrypt

print(encrypt_caesar("Python3.6"))
print(decrypt_caesar("Sbwkrq3.6"))
print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))

public, private = generate_keypair(61, 53)
encrypted = encrypt(public, "Python")
print(encrypted)
print(decrypt(private, encrypted))
```

Цезарь и Виженер меняют только английские буквы и сохраняют регистр.
Пробелы, цифры и остальные символы не меняются. В шифре Виженера
ключ продвигается только на английских буквах. Ключ должен содержать
хотя бы одну английскую букву и не может содержать другие символы.

Для RSA выбираются разные простые числа. В готовых функциях из шаблона
число `p * q` должно быть больше кода каждого символа сообщения.
Для примеров с английским и русским текстом подходят 61 и 53.
Готовый интерактивный пример из шаблона запускается командой:

```bash
python src/lab2/rsa.py
```

## Проверки второй лабораторной

```bash
python -m doctest -v src/lab2/caesar.py src/lab2/vigenre.py src/lab2/rsa.py
python -m unittest discover -s tests/lab2 -v
python -m pytest tests/lab2 -q
python -m isort --check-only src/lab2
python -m black --check -l 120 src/lab2
python -m mypy src/lab2
python -m pylint src/lab2 --fail-under=8
```

Локально пройдены 20 примеров doctest и 26 тестов unittest.
Проверка mypy завершилась без ошибок, оценка pylint составила 9.50/10.
Замечания pylint относятся к сохранённому коду RSA и одинаковым
проверкам диапазона букв в шифрах.

Для сдачи используется отдельная ветка `lab2` и pull request `lab2` в `main`.
После загрузки нужно дождаться успешного выполнения GitHub Actions.
