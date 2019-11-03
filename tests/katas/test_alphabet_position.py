import unittest
from parameterized import parameterized

from katas.alphabet_position.alphabet_position import alphabet_position

class AlphabetPosition(unittest.TestCase):

    @parameterized.expand(
        [
            ("The sunset sets at twelve o' clock.", "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        ]
    )
    def test_alphabet_position(self, text, result):
        ""
        assert(alphabet_position(text)) == result