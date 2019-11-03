import unittest
from parameterized import parameterized

from katas.array_diff.array_diff import array_diff

class ArrayDiff(unittest.TestCase):

    @parameterized.expand(
        [
            ([1, 2], [1], [2]),
            ([1, 2, 2], [1], [2, 2]),
            ([1, 2, 2], [2], [1]),
            ([1, 2, 2], [], [1, 2, 2]),
            ([], [1, 2], [])  
        ]
    )
    def test_array_diff(self, first_array, second_array, result):
        ""
        assert(array_diff(first_array, second_array)) == result