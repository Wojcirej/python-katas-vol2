import unittest
from parameterized import parameterized

from katas.rot13.rot13 import rot13

class Rot13(unittest.TestCase):

    @parameterized.expand(
        [
            ("EBG13 rknzcyr.", "ROT13 example."),
            ("This is my first ROT13 excercise!", "Guvf vf zl svefg EBG13 rkprepvfr!")
        ]
    )
    def test_rot13(self, message, result):
        ""
        assert(rot13(message)) == result