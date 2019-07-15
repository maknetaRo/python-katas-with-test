import unittest
from set_alarm import set_alarm

class TestIfSetAlarm(unittest.TestCase):

    def test_set_alarm_is_true(self):
        self.assertEqual(set_alarm(True, True), False)
        self.assertEqual(set_alarm(False, True), False)
        self.assertEqual(set_alarm(False, False), False)
        self.assertEqual(set_alarm(True, False), True)



if __name__ == '__main__':
    unittest.main()
