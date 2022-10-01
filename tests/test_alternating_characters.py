import unittest
from src.alternating_characters import alternating_characters

class TestAlternatingCharacters(unittest.TestCase):
    def test_give_AAAA_should_3(self):
        text = 'AAAA'
        excepted_result = 3
        result = alternating_characters(text)
        self.assertEqual(excepted_result, result)