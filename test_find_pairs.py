import unittest
from f_pairs import duplicates

class TestFindDuplicates(unittest.TestCase):

    def test_count_pairs(self):

        self.assertEqual(duplicates([1, 2, 2]), 1)
        self.assertEqual(duplicates([1000, 1000]), 1)
        self.assertEqual(duplicates([1, 2, 3]), 0)
        self.assertEqual(duplicates([1, 2, 2, 20, 6, 20, 2, 6, 2]), 4)
        self.assertEqual(duplicates([]), 0)
        self.assertEqual(duplicates([54]), 0)
        self.assertEqual(duplicates([0, 0, 0, 0, 0, 0, 0]) , 3)


if __name__ == '__main__':
    unittest.main()