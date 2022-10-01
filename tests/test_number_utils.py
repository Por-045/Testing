from src.number_utils import is_prime_list

import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_5_7_11_not_prime(self):
        prime_list = [1, 2, 3, 5, 7, 11]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_2_3_5_7_11_is_prime(self):
        prime_list = [2, 3, 5, 7, 11]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_n12_7_11_13_not_prime(self):
        prime_list = [-12, 7, 11, 13]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_0_11_13_not_prime(self):
        prime_list = [0, 11, 13]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_19_23_29_is_prime(self):
        prime_list = [19, 23, 29]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_10_12_14_not_prime(self):
        prime_list = [10, 12, 14]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

