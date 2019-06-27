import unittest
from f_grade import final_grade

class TestCalculateFinalGrade(unittest.TestCase):

    def test_final_grade(self):
        self.assertTrue(final_grade(100, 12), 100)
        self.assertTrue(final_grade(99, 0), 100)
        self.assertTrue(final_grade(10, 15), 100)

        self.assertTrue(final_grade(85, 5), 90)
        self.assertEqual(final_grade(55, 3), 75)

        self.assertEqual(final_grade(55, 0), 0)


if __name__ == '__main__':
    unittest.main()