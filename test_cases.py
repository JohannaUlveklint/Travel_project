import unittest
from unittest.mock import patch
from travel import Travel
# How do I import rush_hour from travel?


class MyTestCase(unittest.TestCase):
    def test_rush_hour_lite(self):
        with patch('builtins.input', return_value='y'):
            speed = rush_hour_lite()  # Should I use self.speed here?
        self.assertEqual('40', speed)


if __name__ == '__main__':
    unittest.main()
