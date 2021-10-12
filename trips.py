

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
from travel import Travel
from terminal_color import color_print
import datetime




class Trips:
    logged_trips = []

    @staticmethod  # Can i call on this function from travel?
    def __get_user_input_int(question):
        user_input = 0
        while True:
            color_print('green', question)
            try:
                user_input = int(input())
                if user_input <= 0:
                    color_print('green', 'You have to enter a value greater than 0. Please try again.')
                    continue
                else:
                    break
            except ValueError:
                print("Please enter a number.")
                continue
        return user_input

"""
datetime.datetime(year=year,month=month,day=day,hour=hour)
that will eliminate somethings like months >12 , hours > 23, non-existent leapdays 
(month=2 has max of 28 on non leap years, 29 otherwise, other months have max of 30 or 31 days)
(throws ValueError exception on error)

correctDate = None
try:
    newDate = datetime.datetime(2008,11,42)
    correctDate = True
except ValueError:
    correctDate = False
print(str(correctDate))
"""
    def log_trip(self):
        running = True
        # correct_date = None  # Skip this variable?
        new_date = None  # Should I assign all these?
        _year = None
        _month = None
        _day = None

        while running:
            _year = self.__get_user_input_int('Enter year with four digits: ')
            _month = self.__get_user_input_int('Enter the number of the month with one or two digits: ')
            _day = self.__get_user_input_int('Enter day with one or two digits: ')
            try:
                new_date = datetime.datetime(_year, _month, _day)
                # correct_date = True
                if new_date > datetime.date.today():
                    print('You can not log trips made in the future.')
                    continue
                else:
                    break
            except ValueError:
                # correct_date = False
                print(f'The date {new_date} is not existing, please try again.')
                continue

        _week = self.check_week_number(_year, _month, _day)
        _distance = self.__get_user_input_int('Enter distance: ')  # Validate this one!

        trip = {'year': _year, 'month': _month, 'day': _day, 'week': _week, 'distance': _distance}
        self.logged_trips.append(trip)  # Does this work?
        # https://stackoverflow.com/questions/52630059/python-add-dictionaries-to-list

    @staticmethod
    def check_week_number(year, month, day):
        week = datetime.date(year, month, day).isocalendar().week
        return week  # Check and if ok check make oneliner and if ok incorporate in log_trip

    def get_weekly_training_data(self):
        pass



