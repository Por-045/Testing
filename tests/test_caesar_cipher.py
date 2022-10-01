import unittest
from src.caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):
    def test_give_middle_outz_should_okffng_qwvb(self):
        text = 'middle_outz'
        rotation = 2
        excepted_result = 'okffng_qwvb'
        result = caesar_cipher(text, rotation)
        self.assertEqual(result, excepted_result)

    def test_give_abcdefghijklmnopqrstuvwxyz_should_defghijklmnopqrstuvwxyzabc(self):
        text = 'abcdefghijklmnopqrstuvwxyz'
        rotation = 3
        excepted_result = 'defghijklmnopqrstuvwxyzabc'
        result = caesar_cipher(text, rotation)
        self.assertEqual(result, excepted_result)
    
    def test_give_rgnoutghaiogauiopgzsdklf_should_rgnoutghaiogauiopgzsdklfc(self):
        text = 'rgnoutghaiogauiopgzsdklf'
        rotation = 26
        excepted_result = 'rgnoutghaiogauiopgzsdklf'
        result = caesar_cipher(text, rotation)
        self.assertEqual(result, excepted_result)

    def test_give_jirateep_should_gfoxqbbm(self):
        text = 'jirateep'
        rotation = -3
        excepted_result = 'gfoxqbbm'
        result = caesar_cipher(text, rotation)
        self.assertEqual(result, excepted_result)

    def test_give_JIRATEEP_should_GFOXQBBM(self):
        text = 'JIRATEEP'
        rotation = -3
        excepted_result = 'GFOXQBBM'
        result = caesar_cipher(text, rotation)
        self.assertEqual(result, excepted_result)

