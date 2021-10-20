import unittest
from unittest.mock import patch
from travel import Travel


class MyTestCase(unittest.TestCase):
    def test_rush_hour(self):
        travel = Travel()
        with patch('builtins.input', return_value='y'):
            speed = travel.rush_hour()  # Should I use self.speed here?
        self.assertEqual('40', speed)

    """
        def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')
    """


if __name__ == '__main__':
    unittest.main()
