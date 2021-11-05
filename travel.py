import datetime
import json

import requests
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
        """
        Called by get_distance_and_duration(). Gets latitude and longitude for chosen addresses using Nominatim.
        :return: self.from_lat, self.from_long, self.to_lat, self.to_long
        """
        geolocator = Nominatim(user_agent="my_application", timeout=15)
        from_address = input('Enter <street> <street number> <city> of your start destination or try a public place: ')
        # from_address = 'Övre Hallegatan 50 Göteborg'
        from_location = geolocator.geocode(from_address)
        self.from_lat = str(from_location.latitude)
        self.from_long = str(from_location.longitude)

        to_address = input('Enter <street> <street number> <city> of your end destination or try a public place: ')
        # to_address = 'Anders Personsgatan 14 Göteborg'
        to_location = geolocator.geocode(to_address)
        self.to_lat = str(to_location.latitude)
        self.to_long = str(to_location.longitude)

        return self.from_lat, self.from_long, self.to_lat, self.to_long

    def get_route(self):
        """
        Called by get_distance_and_duration(). Using Open Route Service API to get routes between a and b by car,
        regular bike and electric bike.
        :return: list with json-files
        """
        api_key = "5b3ce3597851110001cf6248d62eca3e4d314dba96c2e5596a0f8074"

        if not all([self.from_long, self.from_lat, self.to_long, self.to_lat]):  # If any is missing values (=None)
            print("Missing geo-coordinates")
            return None, None, None

        search = f'api_key={api_key}&start={self.from_long},{self.from_lat}&end={self.to_long},{self.to_lat}'
        base_url = 'https://api.openrouteservice.org/v2/directions/'
        vehicles = ['driving-car', 'cycling-regular', 'cycling-electric']

        response = [requests.get(f"{base_url}{v}?" + search) for v in vehicles]
        for i in response:
            if not i.ok:
                return 'Bad Request!'
        response = [line.json() for line in response]
        return response

    def get_distance_and_duration(self):
        """
        Called by print_route_data(). Reads distance and duration from json-file for chosen route by car,
        regular bike and electric bike.
        :return: car_distance, reg_bike_distance, elect_bike_distance, car_duration, reg_bike_duration, elect_bike_duration
        """
        self.get_lat_and_long()
        car_route, reg_bike_route, elect_bike_route = self.get_route()
        # Make as loop?
        car_distance = car_route['features'][0]['properties']['segments'][0]['distance']
        reg_bike_distance = reg_bike_route['features'][0]['properties']['segments'][0]['distance']
        elect_bike_distance = elect_bike_route['features'][0]['properties']['segments'][0]['distance']

        car_duration = car_route['features'][0]['properties']['segments'][0]['duration']
        reg_bike_duration = reg_bike_route['features'][0]['properties']['segments'][0]['duration']
        elect_bike_duration = elect_bike_route['features'][0]['properties']['segments'][0]['duration']

        return car_distance, reg_bike_distance, elect_bike_distance, car_duration, reg_bike_duration, elect_bike_duration

    def print_route_data(self):
        """
        Called by run() case 1 in presentation.py. Shows map of route (by car), a weather forecast and the distance and
        duration for the route made by car, regular bike and electric bike. Prints the differences in duration and CO2
        emissions if going by car.
        :return: ?
        """
        cd, rbd, ebd, cdu, rbdu, ebdu = self.get_distance_and_duration()

        map_url = self.get_map(self.from_lat, self.from_long, self.to_lat, self.to_long)
        clipboard.copy(map_url)
        print('Please open a web browser and enter Ctrl + V to see your trip on a map!')
        input()

        self.print_forecast_data()
        # input()

        color_print('red', '\nCar:')
        print('====')
        print(f'Car distance {self.m_to_km(cd):.3f} km.\nCar duration {self.sec_converter(cdu)}.')
        color_print('yellow', 'Electric Bike:')
        print('==============')
        print(f'Electric bike distance {self.m_to_km(ebd):.3f} km.\nElectric bike duration {self.sec_converter(ebdu)}.')
        color_print('green', 'Regular Bike:')
        print('=============')
        print(f'Regular bike distance {self.m_to_km(rbd):.3f} km.\nRegular bike duration {self.sec_converter(rbdu)}.')
        print('==============================')

        # Change bold to colors?
        print(f'If you go this trip by bike you only would have to add '
              f'' + '\033[1m' + f'{self.sec_converter(rbdu) - self.sec_converter(cdu)}' + '\033[0m' + ' to your travel '
              'time. '
              'Or ' + '\033[1m' + f'{self.sec_converter(ebdu) - self.sec_converter(cdu)} ' + '\033[0m' +
              'if you are electric. :)')
        print('Furthermore, extra time for rush hour traffic and finding a parking lot should be accounted for when '
              'calculating total travel time by car.')
        print('\nCycling ' + '\033[1m' + f'strengthens your body' + '\033[0m' + ' and ' + '\033[1m' +
              'increases spare time' + '\033[0m' + ' since you workout and travel at the same time.')
        print(f'You also will have ' + '\033[1m' + f'cut your CO2 emission with {round((cd * 0.12), 2)} grams' +
              '\033[0m' + ' one way (calculated on an average new car)! That is ' + '\033[1m' +
              f'{round((cd * 0.12 * 43 / 1000), 2)} kg' + '\033[0m' + ' if you are commuting a whole month.')
        print('\nLiving without a car saves an average of 2.4 tons of CO2 equivalents each year.')
        print('If we are to live sustainable we can only emit 3 tons of CO2 equivalents per person and year.')
        print('\033[1m' + 'You can save the world by bike!')
        color_print('magenta', '\033[1m' + 'So Whats __init__ For You?' + '\033[0m' + ' A stronger body, more spare '
                    'time and a super hero cape. The choice is yours.')

        return cd, rbd, ebd, cdu, rbdu, ebdu  # Shall I return anything?

    @staticmethod
    def get_map(from_lat, from_long, to_lat, to_long):
        """
        Called by get_distance_and_duration(). Gets a url for a map with the route made by car.
        :param from_lat: float
        :param from_long: float
        :param to_lat: float
        :param to_long: float
        :return: response.url or 'Bad Request!'
        """
        base_url = 'https://www.mapquestapi.com/staticmap/v5/map?start='
        api_key = 'v2ndcyw0ByFQHDe5LEHCSbtCmvgcJ8cn'
        response = requests.get(f'{base_url}{from_lat},{from_long}&end={to_lat},{to_long}&size=600,400@2x&key='
                                f'{api_key}')
        if response.ok:
            return response.url
        else:
            return 'Bad Request!'

    @staticmethod
    def sec_converter(time_in_sec):
        time = datetime.timedelta(seconds=time_in_sec)
        time_without_ms = time - datetime.timedelta(microseconds=time.microseconds)
        return time_without_ms

    @staticmethod
    def m_to_km(meter):
        km = meter / 1000
        return km

    def get_forecast_data(self):
        """
        Called by print_forecast_data(). Get current weather and a forecast with Open Weather Map API.
        :return: response.json or 'Bad Request!'
        """
        key = 'ab4bdc6adfd6dc3dbe1e9c8ee0b87537'
        base = 'https://api.openweathermap.org/data/2.5/onecall?lat='
        response = requests.get(f'{base}{self.from_lat}&lon={self.from_long}&exclude=minutely,hourly,alerts&units=metric&appid={key}')
        if response.ok:
            return response.json()
        else:
            return 'Bad Request! No weather forecast was found.'

    def print_forecast_data(self):
        """
        Called by print_route_data(). Prints weather and expected precipitation (rain) for current day. If it is no rain
        expected in today's forecast the ['rain']-post is let out and raises an exception which has to be handled for.
        :return: None
        """
        data = self.get_forecast_data()
        color_print('blue', 'Current weather:')
        print(f"Type: {data['current']['weather'][0]['description']}")
        print(f"Degrees: {data['current']['temp']} °C")
        print(f"Wind: {self.deg_to_compass(data['current']['wind_deg'])} {data['current']['wind_speed']} m/s")
        if 'rain' in data['daily'][0]:
            print(f"Expected rain today: {data['daily'][0]['rain']} mm")
        else:
            print("No expected rain in today's forecast.")

    @staticmethod
    def deg_to_compass(num):
        """
        Called by print_forecast_data(). Translate wind degrees into compass points.
        :param num: int
        :return: compass point (string)
        """
        val = int(num / 45)
        arr = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        return arr[(val % 8)]
