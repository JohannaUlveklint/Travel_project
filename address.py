from geopy.geocoders import Nominatim
from terminal_color import color_print


class Address:
    def __init__(self, latitude=None, longitude=None):
        self.latitude = latitude
        self.longitude = longitude

    def get_lat_and_long(self):
        geolocator = Nominatim(user_agent="my_application")
        address = input(color_print('green', 'Enter <street> <street number> <city>'))
        location = geolocator.geocode(address)
        self.latitude = location.latitude
        self.longitude = location.longitude
        return self.latitude, self.longitude  # I return two variables but it still prints 'None'

def main():
    address = Address()
    address.get_lat_and_long()
    print(address.latitude)
    print(address.longitude)


if __name__ == '__main__':
    main()
