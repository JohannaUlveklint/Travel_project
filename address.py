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

    def seconds(self, response):
        seconds = 0
        for i in response:
            if i == 'duration':
                seconds += i
        return seconds

    def sec_to_hh_mm_ss(self, time_in_sec):
        hh_mm_ss = (datetime.timedelta(seconds=time_in_sec))
        return hh_mm_ss


def main():
    address = Address()
    address.get_lat_and_long()

    #
    # bike_request = urllib.request.Request(bike_url)
    # bike_response = urllib.request.urlopen(bike_request)
    # print(bike_response.read())
    #
    # r = car_response.read().decode(encoding="utf-8")
    # result = json.loads(r)
    #
    # itinerary_items = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]
    #
    # for item in itinerary_items:
    #     print(item["instruction"]["text"])

    api_key = "5b3ce3597851110001cf6248d62eca3e4d314dba96c2e5596a0f8074"
    car_url = "https://api.openrouteservice.org/v2/directions/driving-car?api_key=" + api_key + "&start=" + \
              address.from_long + "," + address.from_lat + "&end=" + address.to_long + "," + address.to_lat + ""
    bike_regular_url = "https://api.openrouteservice.org/v2/directions/cycling-regular?api_key=" + api_key + "&start=" +\
                       address.from_long + "," + address.from_lat + "&end=" + address.to_long + "," + address.to_lat + ""
    bike_electric_url = "https://api.openrouteservice.org/v2/directions/cycling-electric?api_key=" + api_key + \
                        "&start=" + address.from_long + "," + address.from_lat + "&end=" + address.to_long + "," + address.to_lat + ""

    car_request = urllib.request.Request(car_url)
    car_response = urllib.request.urlopen(car_request)
    decoded = car_response.read().decode(encoding="utf-8")  # What´s the difference between decoded and result?
    result = json.loads(decoded)
    print(result)
    print(decoded)

    # ['features']['properties']['segments']['duration'] is not [1][2][0][1]: string index out of range
    time_in_sec = decoded['features']['properties']['segments']['duration']
    print(time_in_sec)





if __name__ == '__main__':
    main()
