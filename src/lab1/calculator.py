"""Консольный калькулятор."""


def calculate(first: float, second: float, operation: str) -> float:
    """Выполняет одно арифметическое действие."""
    if operation == "+":
        return first + second
    if operation == "-":
        return first - second
    if operation == "*":
        return first * second
    if operation == "/":
        if second == 0:
            raise ZeroDivisionError("Делить на ноль нельзя")
        return first / second
    raise ValueError("Неизвестная операция")


def main() -> None:
    """Читает ввод и выводит результат."""
    print("Калькулятор")
    while True:
        operation = input("Операция (+, -, *, /) или q для выхода: ").strip()
        if operation == "q":
            break
        if operation not in ("+", "-", "*", "/"):
            print("Неизвестная операция")
            continue

        try:
            first = float(input("Первое число: "))
            second = float(input("Второе число: "))
        except ValueError:
            print("Введите число. Для дробной части используйте точку.")
            continue

        try:
            result = calculate(first, second, operation)
            print("Результат:", result)
        except ZeroDivisionError as error:
            print(error)


if __name__ == "__main__":
    main()
