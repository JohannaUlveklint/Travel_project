import unittest
from unittest.mock import patch
from travel import Travel


class MyTestCase(unittest.TestCase):
    def test_rush_hour(self):
        travel = Travel()
        with patch('builtins.input', return_value='y'):
            speed = travel.rush_hour()  # Should I use self.speed here?
        self.assertEqual('40', speed)


if __name__ == '__main__':
    unittest.main()
