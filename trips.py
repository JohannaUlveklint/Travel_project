from terminal_color import color_print
import datetime
from travel import Travel


class Trips:
    def __init__(self):
        self.logged_trips = []

    @staticmethod
    def __get_user_input_int(question):
        user_input = 0
        while True:
            color_print('green', question)
            try:
                user_input = int(input())
                if user_input <= 0:
                    color_print('green', 'You have to enter a integer value greater than 0. Please try again.')
                    continue
                else:
                    break
            except ValueError:
                print("Please enter a integer number.")
                continue
        return user_input

    def log_trip(self):
        running = True
        year = None
        month = None
        day = None

        while running:
            year = self.__get_user_input_int('\nEnter year with four digits: ')
            month = self.__get_user_input_int('Enter the number of the month with one or two digits: ')
            day = self.__get_user_input_int('Enter day with one or two digits: ')
            try:
                new_date = datetime.datetime(year, month, day)
                if new_date > datetime.datetime.now():
                    print('You can not log trips made in the future.')
                    continue
                else:
                    break
            except ValueError:
                print(f'The date {year}-{month}-{day} is invalid, please try again.')
                continue

        week = datetime.date(year, month, day).isocalendar().week
        bike_type = input(color_print('green', 'Are you riding a [r]egular or [e]lectric bike? Choose [e] if you '
                                               'are a fast biker.'))  # Skip color_print since it prints None?
        travel = Travel()
        while True:
            if bike_type.lower() == 'r':
                distance, duration = travel.get_distance_and_duration()[1][4]
                break
            elif bike_type.lower() == 'e':
                distance, duration = travel.get_distance_and_duration()[2][5]
                break
            else:
                color_print('red', 'Please choose [r] for regular or [e] for electric.')

        trip = {'year': year, 'month': month, 'day': day, 'week': week, 'distance': distance, 'duration': duration}  # Add emissions?
        print(trip)
        self.logged_trips.append(trip)

    def print_trip(self):
        pass

    def get_weekly_training_data(self):
        pass



