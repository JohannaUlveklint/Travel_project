import requests
from geopy.geocoders import Nominatim
from terminal_color import color_print
import urllib.request
import json
import openrouteservice
from openrouteservice import convert
import datetime



"""
https://www.bingmapsportal.com/Application
https://docs.microsoft.com/en-us/bingmaps/rest-services/routes/calculate-a-route?redirectedfrom=MSDN
"""


class Address:
    def __init__(self, from_latitude=None, from_longitude=None, to_latitude=None, to_longitude=None):
        self.from_lat = from_latitude
        self.from_long = from_longitude
        self.to_lat = to_latitude
        self.to_long = to_longitude

    def get_lat_and_long(self):
        geolocator = Nominatim(user_agent="my_application", timeout=10)
        from_address = input('Enter <street> <street number> <city> of your start destination: ')
        # address = input(color_print('green', 'Enter <street> <street number> <city>'))
        # I return two variables but it prints 'None' here, why?
        from_location = geolocator.geocode(from_address)
        self.from_lat = str(from_location.latitude)
        self.from_long = str(from_location.longitude)

        to_address = input('Enter <street> <street number> <city> of your end destination: ')
        to_location = geolocator.geocode(to_address)
        self.to_lat = str(to_location.latitude)
        self.to_long = str(to_location.longitude)
        return self.from_lat, self.from_long, self.to_lat, self.to_long

    # def seconds(self, response):
    #     seconds = 0
    #     for i in response:
    #         if i == 'duration':
    #             seconds += i
    #     return seconds

    def get_url(self, from_long=None, from_lat=None, to_long=None, to_lat=None):
        api_key = "5b3ce3597851110001cf6248d62eca3e4d314dba96c2e5596a0f8074"
        search = str('api_key=' + api_key + '&start=' + from_long + ',' + from_lat + '&end=' + \
                 to_long + ',' + to_lat)
        car_url = requests.get(f"https://api.openrouteservice.org/v2/directions/driving-car?" + search).json()
        reg_bike_url = requests.get(f"https://api.openrouteservice.org/v2/directions/cycling-regular?" + search).json()
        elect_bike_url = requests.get(f"https://api.openrouteservice.org/v2/directions/cycling-electric?" + search).json()
        return car_url, reg_bike_url, elect_bike_url

    def get_distance_and_duration(self, car_url=None, reg_bike_url=None, elect_bike_url=None):
        self.get_lat_and_long()
        self.get_url()
        car_distance = car_url['features'][0]['properties']['segments'][0]['distance']
        reg_bike_distance = reg_bike_url['features'][0]['properties']['segments'][0]['distance']
        elect_bike_distance = elect_bike_url['features'][0]['properties']['segments'][0]['distance']

        car_duration = car_url['features'][0]['properties']['segments'][0]['duration']
        reg_bike_duration = reg_bike_url['features'][0]['properties']['segments'][0]['duration']
        elect_bike_duration = elect_bike_url['features'][0]['properties']['segments'][0]['duration']

        return car_distance, reg_bike_distance, elect_bike_distance, car_duration, reg_bike_duration, elect_bike_duration

    @staticmethod
    def sec_to_hh_mm_ss(time_in_sec):
        hh_mm_ss = (datetime.timedelta(seconds=time_in_sec))
        return hh_mm_ss


def main():
    address = Address()
    address.get_distance_and_duration()
    print(address.car_distance, address.reg_bike_distance, address.elect_bike_distance, address.car_duration,
          address.reg_bike_duration, address.elect_bike_duration)

    # api_key = "5b3ce3597851110001cf6248d62eca3e4d314dba96c2e5596a0f8074"
    # search = 'api_key=' + api_key + '&start=' + address.from_long + ',' + address.from_lat + '&end=' + \
    #          address.to_long + ',' + address.to_lat
    #
    # url = requests.get(f"https://api.openrouteservice.org/v2/directions/" + vehicle + "?" + search).json()
    # distance = url['features'][0]['properties']['segments'][0]['distance']
    # duration = url['features'][0]['properties']['segments'][0]['duration']
    # print(distance)
    # print(duration)
    #
    # car_url = "https://api.openrouteservice.org/v2/directions/driving-car?api_key=" + api_key + "&start=" + \
    #           address.from_long + "," + address.from_lat + "&end=" + address.to_long + "," + address.to_lat + ""
    # bike_regular_url = "https://api.openrouteservice.org/v2/directions/cycling-regular?api_key=" + api_key + "&start=" +\
    #                    address.from_long + "," + address.from_lat + "&end=" + address.to_long + "," + address.to_lat + ""
    # bike_electric_url = "https://api.openrouteservice.org/v2/directions/cycling-electric?api_key=" + api_key + \
    #                     "&start=" + address.from_long + "," + address.from_lat + "&end=" + address.to_long + "," + address.to_lat + ""
    #
    #

if __name__ == '__main__':
    main()
