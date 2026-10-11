import unittest

from src.performance_demo import rank_values


class RankValuesTests(unittest.TestCase):
    def test_prime_values_are_ranked_by_divisor_total(self):
        self.assertEqual(
            rank_values([2, 3, 7, 5, 11, 4, 9]),
            [(2, 3), (3, 4), (5, 6), (7, 8), (11, 12)],
        )

    def test_non_prime_values_are_ignored(self):
        self.assertEqual(rank_values([4, 8, 9, 10]), [])


if __name__ == '__main__':
    unittest.main()
