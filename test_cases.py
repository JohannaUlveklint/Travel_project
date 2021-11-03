import datetime
import json
import os
import unittest
from unittest.mock import patch, mock_open, call, Mock

import trips
from travel import Travel
from statistics import Statistics
from trips import Trips


class TestTravel(unittest.TestCase):
    travel = Travel()
    statistics = Statistics()
    trips = Trips()

    def test_m_to_km(self):
        answer = round(self.travel.m_to_km(5316.2), 3)
        wanted = round(5.3162, 3)
        self.assertEqual(answer, wanted)

    def test_sec_converter(self):
        minutes = str(self.travel.sec_converter(1066.4))
        self.assertEqual(minutes, '0:17:46')

    def test_deg_to_compass(self):
        compass_point = str(self.travel.deg_to_compass(270))
        self.assertEqual(compass_point, 'W')

    def test_save_to_json(self):
        sample_json = {
                "year": 2021,
                "month": 5,
                "day": 3,
                "week": 18,
                "distance": 5316.2,
                "duration": 1066.4
            }
        with patch('builtins.input', return_value='test_data'):  # Mocks input in save_to_json()
            self.trips.save_to_json(sample_json)
            loaded = self.statistics.load_file()
        self.assertEqual([sample_json], loaded)
        os.remove('saved_trips/test_data.json')

    """
        def saved_emissions(self):
        data = self.load_file()
        emissions = 0
        for line in data:
            emissions += round((self.m_to_km(line['distance'] * 0.12)), 2)
        color_print('yellow', f'\nBy making all your trips by bike you have saved {emissions} kg CO2 equivalents!')
    """

    def test_print_map(self):
        with patch('travel.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.url = 'Success!'

            self.get_coordinates()
            url = self.travel.get_map(self.travel.from_lat, self.travel.from_long, self.travel.to_lat,
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
            mocked_get.return_value.ok = False
            mocked_get.return_value.text = 'Bad Request!'

            self.get_coordinates()
            url = self.travel.get_route()
            mocked_get.assert_called_with(f'https://api.openrouteservice.org/v2/directions/cycling-electric?api_key=5b3ce3597851110001cf6248d62eca3e4d314dba96c2e5596a0f8074&start={self.travel.from_long},{self.travel.from_lat}&end={self.travel.to_long},{self.travel.to_lat}')
            self.assertEqual(url, 'Bad Request!')


if __name__ == '__main__':
    unittest.main()
