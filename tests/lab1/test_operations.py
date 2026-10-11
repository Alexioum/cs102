"""Проверки калькулятора."""

import io
import unittest
from unittest.mock import patch

from src.lab1.calculator import calculate, main


class OperationsTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, 3, "+"), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(2, 5, "-"), -3)

    def test_multiplication(self):
        self.assertEqual(calculate(-4, 3, "*"), -12)

    def test_division(self):
        self.assertEqual(calculate(7, 2, "/"), 3.5)

    def test_fractions(self):
        self.assertAlmostEqual(calculate(0.1, 0.2, "+"), 0.3)

    def test_zero(self):
        self.assertEqual(calculate(0, 5, "/"), 0)
        self.assertEqual(calculate(9, 0, "*"), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(5, 0, "/")

    def test_unknown_operation(self):
        with self.assertRaises(ValueError):
            calculate(2, 3, "^")

    def test_several_calculations(self):
        with patch("builtins.input", side_effect=["+", "2", "3", "/", "7", "2", "q"]):
            with patch("sys.stdout", new_callable=io.StringIO) as output:
                main()
        self.assertIn("Результат: 5.0", output.getvalue())
        self.assertIn("Результат: 3.5", output.getvalue())

    def test_errors_do_not_stop_program(self):
        answers = ["?", "+", "abc", "/", "5", "0", "*", "2", "4", "q"]
        with patch("builtins.input", side_effect=answers):
            with patch("sys.stdout", new_callable=io.StringIO) as output:
                main()
        self.assertIn("Неизвестная операция", output.getvalue())
        self.assertIn("Введите число", output.getvalue())
        self.assertIn("Делить на ноль нельзя", output.getvalue())
        self.assertIn("Результат: 8.0", output.getvalue())

    def test_exit(self):
        with patch("builtins.input", side_effect=["q"]):
            with patch("sys.stdout", new_callable=io.StringIO) as output:
                main()
        self.assertNotIn("Результат:", output.getvalue())
