import unittest
from src.grid_challenge import grid_challenge

class TestGridChallenge(unittest.TestCase):
    def test_give_abc_lmp_qrt_should_yes(self):
        grid = ['abc', 'lmp', 'qrt']
        excepted_result = 'YES'
        result = grid_challenge(grid)
        self.assertEqual(result, excepted_result)

    def test_give_mpxz_abcd_wlmf_should_yes(self):
        grid = ['mpxz', 'abcd', 'wlmf']
        excepted_result = 'NO'
        result = grid_challenge(grid)
        self.assertEqual(result, excepted_result)

    def test_give_ebacd_fghij_olmkn_trpqs_xywuv_should_yes(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        excepted_result = 'YES'
        result = grid_challenge(grid)
        self.assertEqual(result, excepted_result)