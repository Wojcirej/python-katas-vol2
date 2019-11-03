import unittest
from parameterized import parameterized

from katas.find_parity_outlier.find_parity_outlier import find_parity_outlier

class FindParityOutlier(unittest.TestCase):

    @parameterized.expand(
        [
            ([2, 4, 6, 8, 10, 3], 3),
            ([2, 4, 0, 100, 4, 11, 2602, 36], 11),
            ([160, 3, 1719, 19, 11, 13, -21], 160)
        ]
    )
    def test_find_parity_outlier(self, integers, result):
        ""
        assert(find_parity_outlier(integers)) == result