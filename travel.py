from terminal_color import color_print


class Travel:
    def __init__(self):  # Do I need all these variables in __init__?
        self.distance = 0
        self.walking_time = 0
        self.speed = 1
        self.changing_time = 0
        self.search_parking_time = 0
        self.time_car = 0
        self.time_bike = 0
        self.cut_emissions = 0

    @staticmethod
    def __get_user_input_float(question):
        user_input = 0
        while True:
            color_print('green', question)
            try:
                user_input = float(input())
                if user_input <= 0:
                    color_print('green', 'You have to enter a value greater than 0. Please try again.')
                    continue
                else:
                    break
            except ValueError:
                print("Please enter a number.")
                continue
        return user_input

    def travel_questions(self):
        # The function does not have to return a value since it´s stored in self.distance and self.walking_time
        to_vehicle = None
        to_end_destination = None

        self.distance = self.__get_user_input_float('How long is the distance you want to travel? Please answer in km.')
        to_vehicle = self.__get_user_input_float('How many minutes walk is it to your car or bike? ')
        to_end_destination = self.__get_user_input_float('How many minutes walk is it from where you parked to your '
                                                   'end destination?')

        self.walking_time = to_vehicle + to_end_destination
        print(self.distance, self.walking_time)

    def time_by_car(self):  # Why does it not store the self.speed values and other similar values?
        color_print('green', '\nWe start by calculating the travel time if you go by car.')
        self.rush_hour()

        color_print('yellow', f'The expected average speed including stopping for traffic lights will be '
                              f'{self.speed} km/h.')
        color_print('yellow', f'{self.search_parking_time} minutes for looking for a parking lot will be added '
                              f'to the total time.')
        self.time_car = (self.distance / self.speed) * 60 + self.walking_time + self.search_parking_time
        color_print('magenta', f'If you go this distance by car the total estimated travel time is {self.time_car} '
                               f'minutes.')
        return self.time_car  # Do I need to return time? Will I use that variable in future statistics?

    def rush_hour(self):
        rush_hour = input('Are you going to drive within rush hours? y/n ')
        while rush_hour.lower() not in 'yn':  # Searches through the string to find a variable match
            rush_hour = input('Are you going to drive within rush hours? Please type [y] for yes or [n] for no: ')

        if rush_hour.lower() == 'y':
            self.speed = 40
            print(self.speed)
            self.search_parking_time = 10
        else:
            self.speed = 50
            print(self.speed)
            self.search_parking_time = 5
            print(self.search_parking_time)

    def time_by_bike(self):
        color_print('green', '\nNow we are going to calculate the travel time if you go by bike.')
        color_print('green', 'But before we can do that we have a question for you:')
        self.cycling_style()

        self.time_bike = (self.distance / self.speed) * 60 + self.walking_time + self.changing_time
        color_print('magenta', f'If you go this distance by bike the total estimated travel time is {self.time_bike} '
                               f'minutes.')
        return self.time_bike  # Do I need to return time?

    def cycling_style(self):
        cycling_style = None
        while cycling_style != 'moderate' and cycling_style != 'fast':
            cycling_style = input('Do you consider yourself a [m]oderate or [f]ast cyclist? ')
            if cycling_style == 'm':
                cycling_style = 'moderate'
                self.speed = 15
                self.changing_time = 0
            elif cycling_style == 'f':
                cycling_style = 'fast'
                self.speed = 20
                self.changing_time = 5
                color_print('yellow', 'Five minutes for change from training clothes will be included.')
            else:
                color_print('green', 'Please choose "m" for moderate tempo cyclist or "f" for fast cyclist.')

        color_print('yellow', f'The expected average speed including stopping '
                              f'for traffic lights will be {self.speed} km/h.')

    def compare_bike_and_car(self):
        self.time_by_car()
        self.time_by_bike()
        self.cut_emissions = self.distance * 0.124
        comparison = self.time_bike - self.time_car  # Not sure this will work, maybe it is 0 - 0 ...
        color_print('magenta', f'The trip is estimated to take {comparison} minutes more by bike.')

        color_print('yellow', f'If you go by bike you will cut your CO2 emission by {self.cut_emissions} kg on '
                              f'this trip only (if your car uses fossil fuels)!')
        # Add sleep and line feed at convenient places for better readability
        color_print('yellow', 'In addition you will also approve your health.')
        color_print('yellow', 'WHO recommends 150 minutes of active training/week, that is 30 minutes five days a '
                              'week.')
        color_print('yellow', f'If you see the trip as one of your physical activities going by bike added your '
                              f'spare time with {self.time_bike} minutes!')

