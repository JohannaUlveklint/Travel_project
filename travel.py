from terminal_color import color_print
from trips import Trips


class Travel:
    def __init__(self):
        self.distance = 0
        self.walking_time = 0
        self.speed = 1
        self.changing_time = 0
        self.search_parking_time = 0

    @staticmethod
    def __get_user_input(question):
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

        self.distance = self.__get_user_input('How long is the distance you want to travel? Please answer in km. ')
        to_vehicle = self.__get_user_input('How many minutes walk is it to your car or bike? ')
        to_end_destination = self.__get_user_input('How many minutes walk is it from where you parked to your '
                                                   'end destination? ')

        self.walking_time = to_vehicle + to_end_destination
        print(self.distance, self.walking_time)

    def time_by_car(self):  # Why does it not store the self.speed values and other similar values?
        color_print('green', '\nWe start by calculating the travel time if you go by car.')
        self.rush_hour()

        color_print('yellow', f'The expected average speed including stopping for traffic lights will be '
                              f'{self.speed} km/h.')
        color_print('yellow', f'{self.search_parking_time} minutes for looking for a parking lot will be added '
                              f'to the total time.')
        time = (self.distance / self.speed) * 60 + self.walking_time + self.search_parking_time
        color_print('magenta', f'If you go this distance by car the total estimated travel time is {time} minutes.')
        return time  # Do I need to return time? Will I use that variable in future statistics?

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

        time = (self.distance / self.speed) * 60 + self.walking_time + self.changing_time
        color_print('magenta', f'If you go this distance by bike the total estimated travel time is {time} minutes.')
        return time  # Do I need to return time?

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
