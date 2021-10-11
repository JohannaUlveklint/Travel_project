import datetime

# Plan Trips. Add trips in dict keyed by date and time, distance, elapsed time.
#
# List for trips arranged by (month or) week, import time? From that list make a track record.
"""
datetime.date has a isocalendar() method, which returns a tuple containing the calendar week:

>>> import datetime
>>> datetime.date(2010, 6, 16).isocalendar()[1]
24
datetime.date.isocalendar() is an instance-method returning a tuple containing year, 
weeknumber and weekday in respective order for the given date instance.

In Python 3.9+ isocalendar() returns a namedtuple with the fields year, week and weekday 
which means you can access the week explicitly using a named attribute:
>>> datetime.date(2010, 6, 16).isocalendar().week
24
"""
from terminal_color import color_print


class Trips:
    logged_trips = []

    @staticmethod  # Can i call on this function from travel?

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

    def log_trip(self):
        _year = input(color_print('green', 'Enter year: '))
        _month = input(color_print('green', 'Enter month: '))
        _day = input(color_print('green', 'Enter day: '))
        _week = self.check_week_number(_year, _month, _day)
        _distance = input(color_print('green', 'Enter distance: '))
        # Check that correct input is made as in travel_questions
        trip = {'year': _year, 'month': _month, 'day': _day, 'week': _week, 'distance': _distance}
        self.logged_trips.append(trip)  # Does this work?
        # https://stackoverflow.com/questions/52630059/python-add-dictionaries-to-list

    @staticmethod
    def check_week_number(year, month, day):
        week = datetime.date(year, month, day)
        return week  # Check and if ok check make oneliner and if ok incorporate in log_trip

    def get_weekly_training_data(self):
        pass



