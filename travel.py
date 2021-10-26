import datetime
import requests
from decimal import Decimal
from geopy.geocoders import Nominatim
import clipboard
from terminal_color import color_print


class Travel:
    def __init__(self, from_latitude=None, from_longitude=None, to_latitude=None, to_longitude=None):
        self.from_lat = from_latitude
        self.from_long = from_longitude
        self.to_lat = to_latitude
        self.to_long = to_longitude

    def get_lat_and_long(self):
        geolocator = Nominatim(user_agent="my_application", timeout=15)
        # from_address = input('Enter <street> <street number> <city> of your start destination: ')
        from_address = 'Övre Hallegatan 50 Göteborg'
        # address = input(color_print('green', 'Enter <street> <street number> <city>'))
        # I return two variables but it prints 'None' here, why?
        from_location = geolocator.geocode(from_address)
        self.from_lat = str(from_location.latitude)
        self.from_long = str(from_location.longitude)

        # to_address = input('Enter <street> <street number> <city> of your end destination: ')
        to_address = 'Anders Personsgatan 14 Göteborg'
        to_location = geolocator.geocode(to_address)
        self.to_lat = str(to_location.latitude)
        self.to_long = str(to_location.longitude)
        return self.from_lat, self.from_long, self.to_lat, self.to_long

    def get_url(self):
        api_key = "5b3ce3597851110001cf6248d62eca3e4d314dba96c2e5596a0f8074"

        if not all([self.from_long, self.from_lat, self.to_long, self.to_lat]):  # If any is missing values (=None)
            print("Missing geo-coordinates")
            return None, None, None
        search = f'api_key={api_key}&start={self.from_long},{self.from_lat}&end={self.to_long},{self.to_lat}'

        base_url = 'https://api.openrouteservice.org/v2/directions/'
        vehicles = ['driving-car', 'cycling-regular', 'cycling-electric']

        # car_url, reg_bike_url, elect_bike_url = [requests.get(f"{base_url}{v}?" + search).json() for v in vehicles]
        # Instead of adding values to the three variables as above we can directly return the comprehension and in
        # get_distance_and_duration() the output will be set to the variables in car_url, reg_bike_url, elect_bike_url
        # = self.get_url()

        return [requests.get(f"{base_url}{v}?" + search).json() for v in vehicles]

    def get_distance_and_duration(self):
        self.get_lat_and_long()
        car_url, reg_bike_url, elect_bike_url = self.get_url()
        # Make as loop?
        car_distance = car_url['features'][0]['properties']['segments'][0]['distance']
        reg_bike_distance = reg_bike_url['features'][0]['properties']['segments'][0]['distance']
        elect_bike_distance = elect_bike_url['features'][0]['properties']['segments'][0]['distance']

        car_duration = car_url['features'][0]['properties']['segments'][0]['duration']
        reg_bike_duration = reg_bike_url['features'][0]['properties']['segments'][0]['duration']
        elect_bike_duration = elect_bike_url['features'][0]['properties']['segments'][0]['duration']

        map_url = self.print_map(self.from_lat, self.from_long, self.to_lat, self.to_long)
        return car_distance, reg_bike_distance, elect_bike_distance, car_duration, reg_bike_duration, \
               elect_bike_duration, map_url

    def print_distance_and_duration(self):
        cd, rbd, ebd, cdu, rbdu, ebdu, map_url = self.get_distance_and_duration()
        clipboard.copy(map_url)
        print('Please open a web browser and enter Ctrl + V to see your trip on a map!')
        input()
        print('Car:')
        print('====')
        print(f'Car distance {self.m_to_km(cd)} km.\nCar duration {self.sec_converter(cdu)}.')
        print('Electric Bike:')
        print('==============')
        print(f'Electric bike distance {self.m_to_km(ebd)} km.\nElectric bike duration {self.sec_converter(ebdu)}.')
        print('Regular Bike:')
        print('=============')
        print(f'Regular bike distance {self.m_to_km(rbd)} km.\nRegular bike duration {self.sec_converter(rbdu)}.')
        print('==============')
        # Change bold to colors?
        print(f'If you go this trip by bike it will actually only take '
              f'' + '\033[1m' + f'{self.sec_converter(rbdu) - self.sec_converter(cdu)} minutes' + '\033[0m' + ' more. '
              'Or ' + '\033[1m' + f'{self.sec_converter(ebdu) - self.sec_converter(cdu)} minutes ' + '\033[0m' +
              'if you are electric. :)')
        print('Furthermore, extra time for rush hour traffic and finding a parking lot should be accounted for when '
              'calculating total travel time by car.')
        print('\nCycling ' + '\033[1m' + f'strengthens your body' + '\033[0m' + ' and ' + '\033[1m' +
              'increases spare time' + '\033[0m' + ' since you workout and travel at the same time.')
        print(f'You also will have ' + '\033[1m' + f'cut your CO2 emission with {round((cd * 0.12), 2)} grams' +
              '\033[0m' + ' one way (calculated on an average new car)! That is ' + '\033[1m' +
              f'{round((cd * 0.12 * 43 / 1000), 2)} kg' + '\033[0m' + ' if you are commuting a whole month.')
        print('\nLiving without a car saves an average of 2.4 tons of CO2 each year. If we are to live sustainable we')
        print('can only emit 3 tons of CO2 per person and year. You can save the world by bike!')
        print('\033[1m' + 'So Whats __init__ For You?' + '\033[0m' + ' A stronger body, more spare time and a super '
                                                                     'hero cape. The choice is yours.')

        return cd, rbd, ebd, cdu, rbdu, ebdu  # Return emissions?

    def print_map(self, from_lat, from_long, to_lat, to_long):
        base_url = 'https://www.mapquestapi.com/staticmap/v5/map?start='
        api_key = 'v2ndcyw0ByFQHDe5LEHCSbtCmvgcJ8cn'
        url = f'{base_url}{from_lat},{from_long}&end={to_lat},{to_long}&size=600,400@2x&key={api_key}'
        return url


    @staticmethod
    def sec_converter(time_in_sec):
        time = datetime.timedelta(seconds=time_in_sec)
        time_without_ms = time - datetime.timedelta(microseconds=time.microseconds)
        return time_without_ms

    @staticmethod
    def m_to_km(meter):
        km = Decimal(meter / 1000).quantize(Decimal("1.000"))
        return km

    # @staticmethod
    # def __get_user_input_float(question):
    #     user_input = 0
    #     while True:
    #         color_print('green', question)
    #         try:
    #             user_input = float(input())
    #             if user_input <= 0:
    #                 color_print('green', 'You have to enter a value greater than 0. Please try again.')
    #                 continue
    #             else:
    #                 break
    #         except ValueError:
    #             print("Please enter a number.")
    #             continue
    #     return user_input





