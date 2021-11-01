import datetime
import unittest
from unittest.mock import patch

from travel import Travel


class TestTravel(unittest.TestCase):
    travel = Travel()

    def test_m_to_km(self):
        answer = round(self.travel.m_to_km(5316.2), 3)
        wanted = round(5.316, 3)
        self.assertEqual(answer, wanted)

    def test_sec_converter(self):
        minutes = str(self.travel.sec_converter(60))
        self.assertEqual(minutes, '0:01:00')


    """
        def print_map(from_lat, from_long, to_lat, to_long):
        base_url = 'https://www.mapquestapi.com/staticmap/v5/map?start='
        api_key = 'v2ndcyw0ByFQHDe5LEHCSbtCmvgcJ8cn'
        response = requests.get(f'{base_url}{from_lat},{from_long}&end={to_lat},{to_long}&size=600,400@2x&key='
                                f'{api_key}')
        if response.ok:
            return response.url
        else:
            return 'Bad Request!'
    """

    def test_print_map(self):
        with patch('travel.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            self.get_coordinates()
            url = self.travel.print_map(self.travel.from_lat, self.travel.from_long, self.travel.to_lat,
                                        self.travel.to_long)
            mocked_get.assert_called_with(f'https://www.mapquestapi.com/staticmap/v5/map?start={self.travel.from_lat},{self.travel.from_long}&end={self.travel.to_lat},{self.travel.to_long}&size=600,400@2x&key=v2ndcyw0ByFQHDe5LEHCSbtCmvgcJ8cn')
            self.assertEqual(url, 'Success!')

    def get_coordinates(self):
        self.travel.from_lat = '57.7183072'
        self.travel.from_long = '11.9381581'
        self.travel.to_lat = '57.7104969'
        self.travel.to_long = '11.9948842'
        return self.travel.from_lat, self.travel.from_long, self.travel.to_lat, self.travel.to_long

    def test_get_url(self):
        with patch('travel.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            self.get_coordinates()
            url = self.travel.get_url()
            mocked_get.assert_called_with(f'https://api.openrouteservice.org/v2/directions/cycling-electric?api_key=5b3ce3597851110001cf6248d62eca3e4d314dba96c2e5596a0f8074&start={self.travel.from_long},{self.travel.from_lat}&end={self.travel.to_long},{self.travel.to_lat}')
            self.assertEqual(url, 'Success!')

            mocked_get.return_value.ok = False

            url = self.travel.get_url()
            mocked_get.assert_called_with(f'https://api.openrouteservice.org/v2/directions/cycling-regular?api_key=5b3ce3597851110001cf6248d62eca3e4d314dba96c2e5596a0f8074&start={self.travel.from_long},{self.travel.from_lat}&end={self.travel.to_long},{self.travel.to_lat}')
            self.assertEqual(url, 'Bad Response!')





if __name__ == '__main__':
    unittest.main()
