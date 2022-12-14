import unittest
from src.alternating_characters import alternating_characters

class TestAlternatingCharacters(unittest.TestCase):
    def test_give_AAAA_should_3(self):
        text = 'AAAA'
        excepted_result = 3
        result = alternating_characters(text)
        self.assertEqual(excepted_result, result)

    def test_give_BBBBB_should_4(self):
        text = 'BBBBB'
        excepted_result = 4
        result = alternating_characters(text)
        self.assertEqual(excepted_result, result)

    def test_give_ABABABAB_should_0(self):
        text = 'ABABABAB'
        excepted_result = 0
        result = alternating_characters(text)
        self.assertEqual(excepted_result, result)
    
    def test_give_BABABA_should_0(self):
        text = 'BABABA'
        excepted_result = 0
        result = alternating_characters(text)
        self.assertEqual(excepted_result, result)

    def test_give_AAABBB_should_0(self):
        text = 'AAABBB'
        excepted_result = 4
        result = alternating_characters(text)
        self.assertEqual(excepted_result, result)