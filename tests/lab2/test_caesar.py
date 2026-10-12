"""Проверки шифра Цезаря."""

import unittest

from src.lab2.caesar import decrypt_caesar, encrypt_caesar


class CaesarTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(encrypt_caesar("Python3.6"), "Sbwkrq3.6")
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), "Python3.6")

    def test_end_of_alphabet(self):
        self.assertEqual(encrypt_caesar("xyzXYZ"), "abcABC")

    def test_zero_shift(self):
        self.assertEqual(encrypt_caesar("Abc", 0), "Abc")

    def test_negative_shift(self):
        self.assertEqual(encrypt_caesar("Abz", -1), "Zay")

    def test_large_shift(self):
        self.assertEqual(encrypt_caesar("Python", 55), "Sbwkrq")

    def test_other_characters(self):
        self.assertEqual(encrypt_caesar("Привет, 123! é"), "Привет, 123! é")

    def test_empty_text(self):
        self.assertEqual(encrypt_caesar(""), "")
        self.assertEqual(decrypt_caesar(""), "")

    def test_round_trip(self):
        text = "Hello, Python3.13!"
        for shift in [-55, -1, 0, 1, 55]:
            self.assertEqual(decrypt_caesar(encrypt_caesar(text, shift), shift), text)
