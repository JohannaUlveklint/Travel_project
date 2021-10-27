import unittest
from unittest.mock import patch
import travel


class TestTravel(unittest.TestCase):
    def test_m_to_km(self):
        self.assertEqual(travel.m_to_km(5316.2), 5.316)
        self.assertEqual(travel.m_to_km(-5316.2), -5.316)

    def test_sec_converter(self):
        self.assertEqual(travel.sec_converter)
    """
            def sec_converter(time_in_sec):
        time = datetime.timedelta(seconds=time_in_sec)
        time_without_ms = time - datetime.timedelta(microseconds=time.microseconds)
    """

    """
       def get_url(self):
        api_key = "5b3ce3597851110001cf6248d62eca3e4d314dba96c2e5596a0f8074"

        if not all([self.from_long, self.from_lat, self.to_long, self.to_lat]):  # If any is missing values (=None)
            print("Mi ing geo-coordinates")
            return None, None, None

        search = f'api_key={api_key}&start={self.from_long},{self.from_lat}&end={self.to_long},{self.to_lat}'
        base_url = 'https://api.openrouteservice.org/v2/directions/'
        vehicles = ['driving-car', 'cycling-regular', 'cycling-electric']

        return [requests.get(f"{base_url}{v}?" + search).json() for v in vehicles]
    """
    # def test_get_url(self):
    #     with patch('travel.requests.get') as mocked_get:
    #         mocked_get.return_value.ok = True
    #         mocked_get.return_value.text = 'Success!'
    #
    #         url = self.get_url()
    #         mocked_get.assert_called_with('https://api.openrouteservice.org/v2/directions/driving-car?api_key='
    #         '5b3ce3597851110001cf6248d62eca3e4d314dba96c2e5596a0f8074&start=11.9381581,57.7183072&end='
    #         '11.9948842,57.7104969')
    #         self.assertEqual(url, 'Success!')
    #
    #         mocked_get.return_value.ok = False
    #
    #         url = self.get_url()
    #         mocked_get.assert_called_with('https://api.openrouteservice.org/v2/directions/driving-car?api_key='
    #                                       '5b3ce3597851110001cf6248d62eca3e4d314dba96c2e5596a0f8074&start=11.9381581,57.7183072&end='
    #                                       '11.9948842,57.7104969')
    #         self.assertEqual(url, 'Success!')


    """
        def monthly_schedule(self, month):
            response = requests.get(f'http://company.com/{self.last}/{month}')
            if response.ok:
                return response.text
            else:
                return 'Bad Request!'
        
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
