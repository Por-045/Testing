import unittest
from src.funny_string import funny_string

class TestFunnyString(unittest.TestCase):
    def test_give_abcd_should_funny(self):
        text = 'abcd'
        excepted_result = 'Funny'
        result = funny_string(text)
        self.assertEqual(result, excepted_result)

    def test_give_ehkl_should_funny(self):
        text = 'ehkl'
        excepted_result = 'Not Funny'
        result = funny_string(text)
        self.assertEqual(result, excepted_result)
