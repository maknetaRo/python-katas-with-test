import unittest
from divisible import divisible_by


class TestDivisibleNumbers(unittest.TestCase):

    def test_numbers_are_list(self):
        self.assertIsInstance(divisible_by([1, 2, 3],  2), list)

    def test_output_is_list(self):
        self.assertIsInstance(divisible_by([1, 2, 3], 2), list)

    def test_numbers_divisible_by(self):
        self.assertCountEqual(divisible_by([1, 2, 3], 2), [2])
        self.assertCountEqual(divisible_by([1, 2, 3, 4, 5, 6], 2), [2, 4, 6])
        self.assertEqual(divisible_by([1, 2, 3, 4, 5, 6], 2), [2, 4, 6])
        self.assertEqual(divisible_by([1,3, 5], 2), [])



if __name__ == '__main__':
    unittest.main()
