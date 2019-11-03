import unittest
from parameterized import parameterized

from katas.guess_my_number.guess_my_number import guess_my_number

class GuessMyNumber(unittest.TestCase):

    @parameterized.expand(
        [
            ('0', '123-451-2345', '###-###-####'),
            ('01', '123-451-2345', '1##-##1-####'),
            ('012', '123-451-2345', '12#-##1-2###'),
            ('0123', '123-451-2345', '123-##1-23##'),
            ('01234', '123-451-2345', '123-4#1-234#'),
            ('012345', '123-451-2345', '123-451-2345'),
        ]
    )
    def test_guess_my_number(self, guess, number, result):
        ""
        assert(guess_my_number(guess, number)) == result