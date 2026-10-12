"""Проверки функций RSA."""

import unittest

from src.lab2.rsa import decrypt, encrypt, gcd, generate_keypair, is_prime, multiplicative_inverse


class RsaTests(unittest.TestCase):
    def test_prime_numbers(self):
        for number in [2, 3, 17, 61, 97]:
            self.assertTrue(is_prime(number))

    def test_nonprime_numbers(self):
        for number in [-7, 0, 1, 4, 9, 25, 49]:
            self.assertFalse(is_prime(number))

    def test_gcd(self):
        for a, b, result in [(12, 15, 3), (3, 7, 1), (-12, 15, 3), (0, 5, 5), (0, 0, 0)]:
            self.assertEqual(gcd(a, b), result)

    def test_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)
        self.assertEqual(multiplicative_inverse(17, 3120), 2753)
        self.assertEqual(multiplicative_inverse(-3, 11), 7)

    def test_no_inverse(self):
        for e, phi in [(6, 12), (0, 7), (7, 1), (7, 0), (7, -40)]:
            with self.assertRaises(ValueError):
                multiplicative_inverse(e, phi)

    def test_keypair(self):
        public, private = generate_keypair(61, 53)
        e, n = public
        d, private_n = private
        self.assertEqual(n, 3233)
        self.assertEqual(private_n, n)
        self.assertEqual(gcd(e, 3120), 1)
        self.assertEqual((e * d) % 3120, 1)

    def test_invalid_primes(self):
        for p, q in [(4, 7), (7, 4), (7, 7), (-3, 7)]:
            with self.assertRaises(ValueError):
                generate_keypair(p, q)

    def test_known_message(self):
        self.assertEqual(encrypt((17, 3233), "A"), [2790])
        self.assertEqual(decrypt((2753, 3233), [2790]), "A")

    def test_round_trip(self):
        public, private = generate_keypair(61, 53)
        for text in ["Python", "Привет!", "", "Aa 0123!?"]:
            self.assertEqual(decrypt(private, encrypt(public, text)), text)
