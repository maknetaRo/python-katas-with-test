import unittest
from invert_values import invert

class TestIvertValues(unittest.TestCase):

    def test_input_is_list(self):
        self.assertIsInstance(invert([1,2,3,4,5]), list)

    def test_output_is_list(self):
        self.assertIsInstance(invert([1,2,3,4,5]), list)

    def test_output_is_invert(self):
        self.assertEqual(invert([1,2,3,4,5]),[-1, -2, -3, -4, -5])
        self.assertEqual(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
        self.assertEqual(invert([]), [])
        self.assertEqual(invert([-111]), [111])


if __name__ == '__main__':
    unittest.main()
