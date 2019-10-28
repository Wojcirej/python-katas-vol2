import unittest
from parameterized import parameterized

from katas.abbreviate_two_word_name.abbreviate_two_word_name import abbreviate_two_word_name

class TestIsDivisible(unittest.TestCase):

    @parameterized.expand(
        [
            ("Sam Smith", "S.S"),
            ("some Name", "S.N"),
            ("Some name", "S.N"),
            ("Sam Harris", "S.H"),
            ("Patrick Feenan", "P.F")
        ]
    )
    def test_abbreviate_two_word_name(self, name, result):
        assert(abbreviate_two_word_name(name)) == result