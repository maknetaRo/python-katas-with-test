import unittest
from bool import boolean_to_string

class TestBooleanCovertToString(unittest.TestCase):

    def test_boolean_to_string(self):

        self.assertEqual(boolean_to_string(True), "True")
        self.assertEqual(boolean_to_string(False), "False")
if __name__ == '__main__':
    unittest.main()