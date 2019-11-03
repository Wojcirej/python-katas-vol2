import unittest
from parameterized import parameterized

from katas.grasshopper_summation.grasshopper_summation import grasshopper_summation

class GrasshopperSummation(unittest.TestCase):

    @parameterized.expand(
        [
            (1, 1),
            (8, 36),
            (22, 253),
            (100, 5050),
            (213, 22791)
        ]
    )
    def test_grasshopper_summation(self, n, result):
        ""
        assert(grasshopper_summation(n)) == result