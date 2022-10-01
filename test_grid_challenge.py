import unittest
from src.grid_challenge import grid_challenge

class TestGridChallenge(unittest.TestCase):
    def test_give_abc_lmp_qrt_should_yes(self):
        grid = ['abc', 'lmp', 'qrt']
        excepted_result = 'YES'
        result = grid_challenge(grid)
        self.assertEqual(result, excepted_result)