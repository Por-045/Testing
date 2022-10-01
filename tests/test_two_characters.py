import unittest
from src.two_characters import two_characters

class TestTwoCharacters(unittest.TestCase):
    def test_give_beabeefeab_should_5(self):
        text = 'beabeefeab'
        excepted_result = 5
        result = two_characters(text)
        self.assertEqual(result, excepted_result)

    def test_give_asdcbsdcagfsdbgdfanfghbsfdab_should_8(self):
        text = 'asdcbsdcagfsdbgdfanfghbsfdab'
        excepted_result = 8
        result = two_characters(text)
        self.assertEqual(result, excepted_result)