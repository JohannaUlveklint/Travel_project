from geopy.geocoders import Nominatim
from terminal_color import color_print
import urllib.request
import json

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


def main():
    address = Address()
    address.get_lat_and_long()
    # print(address.from_lat)
    # print(address.from_long)
    # print(address.to_lat)
    # print(address.to_long)

    bing_maps_key = 'Ao811tzo3TGlB7SiQPhGQwVg31dHk6pTH5BeSAT8swbIWbbY20aHqpkYrJf2Tsg5'
    car_url = "http://dev.virtualearth.net/REST/v1/Routes?wayPoint.1=" + address.from_lat + "," + address.from_long + \
                  "&wayPoint.2=" + address.to_lat + "," + address.to_long + "&key=" + bing_maps_key
    bike_url = "http://dev.virtualearth.net/REST/v1/Routes/Walking?wayPoint.1=" + address.from_lat + "," + \
                  address.from_long + "&wayPoint.2=" + address.to_lat + "," + address.to_long + "&key=" \
                  + bing_maps_key

    car_request = urllib.request.Request(car_url)
    car_response = urllib.request.urlopen(car_request)
    print(car_response.read())

    bike_request = urllib.request.Request(bike_url)
    bike_response = urllib.request.urlopen(bike_request)
    print(bike_response.read())

    r = car_response.read().decode(encoding="utf-8")
    result = json.loads(r)

    itinerary_items = result["resourceSets"][0]["resources"][0]["routeLegs"][0]["itineraryItems"]

    for item in itinerary_items:
        print(item["instruction"]["text"])


if __name__ == '__main__':
    main()
