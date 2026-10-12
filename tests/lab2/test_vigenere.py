"""Проверки шифра Виженера."""

import unittest

from src.lab2.caesar import encrypt_caesar
from src.lab2.vigenre import decrypt_vigenere, encrypt_vigenere


class VigenereTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

    def test_zero_shift(self):
        self.assertEqual(encrypt_vigenere("Python", "a"), "Python")

    def test_case(self):
        self.assertEqual(encrypt_vigenere("AttackAtDawn", "leMon"), "LxfopvEfRnhr")

    def test_spaces_and_punctuation(self):
        self.assertEqual(encrypt_vigenere("Attack at dawn!", "LEMON"), "Lxfopv ef rnhr!")

    def test_one_letter_key(self):
        text = "Python3.13!"
        self.assertEqual(encrypt_vigenere(text, "D"), encrypt_caesar(text))

    def test_long_key(self):
        self.assertEqual(encrypt_vigenere("ABC", "LEMONLEMON"), "LFO")

    def test_empty_text(self):
        self.assertEqual(encrypt_vigenere("", "key"), "")
        self.assertEqual(decrypt_vigenere("", "key"), "")

    def test_invalid_key(self):
        for keyword in ["", "A1", "КЛЮЧ", "é"]:
            with self.assertRaises(ValueError):
                encrypt_vigenere("text", keyword)
            with self.assertRaises(ValueError):
                decrypt_vigenere("text", keyword)

    def test_round_trip(self):
        text = "Hello, Python3.13! Привет"
        self.assertEqual(decrypt_vigenere(encrypt_vigenere(text, "Lemon"), "Lemon"), text)
