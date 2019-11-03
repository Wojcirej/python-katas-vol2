import unittest
from parameterized import parameterized

from katas.total_amount_of_points.total_amount_of_points import total_amount_of_points

class TotalAmountOfPoints(unittest.TestCase):

    @parameterized.expand(
        [
            (['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'], 30),
            (['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4'], 10),
            (['0:1','0:2','0:3','0:4','1:2','1:3','1:4','2:3','2:4','3:4'], 0),
            (['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4'], 15),
            (['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4'], 12),
            (['0:3','2:0','4:3','2:4','4:3','0:2','2:2','3:0','0:1','3:2'], 16),
            (['2:2','1:0','0:2','3:4','0:3','1:2','2:4','3:0','4:0','1:4'], 10),
            (['1:3','4:1','0:4','4:4','1:0','1:0','0:2','1:3','4:4','2:1'], 14),
            (['1:1','0:3','4:4','1:3','4:4','3:2','3:4','1:4','1:2','2:3'], 6),
            (['0:2','3:1','0:4','1:2','3:1','4:2','0:2','4:4','1:0','2:4'], 13),
            (['0:3','0:3','3:2','1:2','0:1','3:1','3:1','3:0','1:0','2:1'], 18),
            (['0:3','4:3','0:3','0:4','1:1','1:3','0:1','0:2','3:0','3:4'], 7),
            (['3:4','2:3','0:2','4:4','1:2','3:2','4:0','3:1','4:1','3:4'], 13),
            (['4:4','2:3','0:1','0:1','2:2','3:2','3:1','1:0','3:2','0:2'], 14),
            (['4:3','4:4','3:4','2:0','1:1','1:4','0:3','1:4','1:3','2:1'], 11),
            (['1:3','3:1','3:0','1:4','0:1','0:3','1:4','0:2','4:2','0:2'], 9),
            (['4:3','3:3','4:3','4:1','2:0','4:0','1:1','2:0','3:2','3:3'], 24),
            (['4:4','0:3','3:2','0:4','4:4','4:3','2:3','2:3','1:1','0:0'], 10),
            (['4:2','0:0','4:0','3:4','4:0','1:1','3:1','0:4','3:4','2:2'], 15),
            (['4:0','4:2','1:2','0:1','1:1','1:4','2:1','4:1','0:1','4:4'], 14),
            (['4:4','0:1','4:3','1:1','1:2','1:4','2:0','1:3','1:3','2:1'], 11),
            (['0:0','0:4','4:3','4:0','2:4','1:4','3:3','2:0','2:3','1:2'], 11),
            (['1:2','2:1','4:0','0:1','3:1','4:0','1:0','3:2','1:3','1:3'], 18),
            (['1:1','1:1','2:4','1:2','3:4','1:4','3:2','1:3','0:4','3:3'], 6),
            (['1:4','1:4','0:2','3:0','2:0','4:0','1:3','2:1','3:1','4:0'], 18),
            (['3:0','4:2','3:4','3:2','1:2','2:0','1:2','3:4','1:0','2:0'], 18),
            (['2:1','1:4','2:2','2:1','1:1','1:0','2:0','3:1','2:2','2:4'], 18),
            (['2:3','3:1','2:3','1:0','1:4','3:4','3:4','0:0','3:4','1:4'], 7),
            (['2:1','3:0','1:0','3:4','1:2','3:4','1:1','2:1','3:1','3:1'], 19),
            (['0:0','2:1','0:4','3:2','2:1','4:1','4:2','2:2','0:0','3:1'], 21),
            (['3:3','0:1','2:3','4:3','4:4','1:0','1:3','1:1','2:3','3:4'], 9),
            (['2:0','0:3','4:1','3:1','2:2','3:0','4:2','3:0','1:0','2:2'], 23),
            (['3:2','3:0','4:1','4:1','3:1','4:4','0:1','0:2','2:0','1:0'], 22),
            (['0:1','2:1','1:1','3:0','3:3','1:4','4:4','2:1','3:1','1:4'], 15),
            (['4:2','4:3','0:3','2:4','2:0','3:2','0:2','3:2','3:1','0:1'], 18),
            (['2:3','4:1','1:3','3:3','4:2','0:2','2:2','3:2','4:2','2:1'], 17),
            (['3:1','0:2','0:1','0:0','2:3','1:2','3:4','2:3','0:3','0:4'], 4),
            (['0:3','0:3','3:4','0:2','0:4','3:2','0:0','1:1','4:1','0:1'], 8),
            (['3:3','0:4','1:2','2:2','3:1','4:3','0:3','2:4','0:2','4:4'], 9),
            (['2:1','1:1','1:3','0:0','2:4','0:0','1:0','2:4','2:3','3:4'], 9),
            (['2:2','4:2','1:4','1:2','3:1','0:4','0:0','1:4','2:4','0:0'], 9),
            (['3:4','0:2','4:0','3:0','1:2','2:1','2:3','0:1','1:4','4:1'], 12),
            (['3:2','3:1','4:0','1:1','3:2','4:0','2:3','3:2','2:4','1:4'], 19),
            (['2:3','3:0','2:3','2:0','3:4','0:4','0:0','2:0','1:3','3:1'], 13),
            (['1:3','1:4','0:1','0:1','0:0','1:2','4:1','2:4','4:4','4:1'], 8),
            (['1:2','0:3','0:2','0:4','3:0','1:2','0:3','3:3','4:4','3:0'], 8),
            (['0:1','3:1','1:0','1:1','1:1','4:2','4:2','2:4','3:0','0:0'], 18),
            (['2:4','0:4','4:2','2:3','1:2','3:2','1:3','2:3','1:3','2:4'], 6),
            (['2:3','0:0','0:4','0:4','2:2','0:1','4:4','4:4','2:4','4:0'], 7),
            (['4:4','2:2','1:0','2:2','1:0','3:0','2:3','2:1','1:1','2:3'], 16),
            (['2:2','3:3','3:2','2:4','0:2','0:0','2:2','0:1','0:0','2:0'], 11),
            (['4:1','1:0','2:1','3:2','3:4','0:4','0:0','2:4','2:4','3:0'], 16),
            (['1:0','3:0','3:1','4:2','4:0','4:2','2:0','4:3','4:4','4:4'], 26),
            (['1:2','4:2','3:3','4:1','4:3','4:2','2:2','1:3','0:0','0:1'], 15),
            (['3:0','3:0','2:0','2:4','4:0','2:1','4:2','1:1','4:0','1:2'], 22),
        ]
    )
    def test_total_amount_of_points(self, games, result):
        ""
        assert(total_amount_of_points(games)) == result