import unittest
from monkeys import monkey_count

class TestCountMonkeys(unittest.TestCase):

    def test_monkey_count(self):
        self.assertEqual(monkey_count(1), [1])
        self.assertEqual(monkey_count(5), [1, 2, 3, 4, 5])

        self.assertEqual(monkey_count(3), [1, 2, 3])
        self.assertEqual(monkey_count(10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])



if __name__ == '__main__':
    unittest.main()
