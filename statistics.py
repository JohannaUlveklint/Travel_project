import json
import datetime
import math

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from trips import Trips
from travel import Travel
from terminal_color import color_print


class Statistics:
    def __init__(self):
        self.data = None
        self.travel = Travel()

    def calc_weekly_distance(self, week):
        """
        The method is being called by compare_weeks().
        :param week: int
        :return: distance (float)
        """
        # data = self.load_file()
        meter = 0
        distance = 0

        for line in self.data:
            if line['week'] == week:
                meter += line['distance']
                distance = self.m_to_km(meter)

        return distance

    def calc_weekly_duration(self, week):
        """
        The method is being called by compare_weeks().
        :param week: int
        :return: duration (float)
        """
        # data = self.load_file()
        # travel = Travel()
        seconds = 0
        duration = 0

        # Print which weeks are in the file

        for line in self.data:
            if line['week'] == week:
                seconds += line['duration']
                # duration = self.travel.sec_converter(seconds)

        return seconds

    def compare_weeks(self):
        """
        Called by run() in presentation.py, case 3. Compares the total distance made by bike each chosen week and shows
        the result in a bar plot.
        :return: ?
        """
        # global num_of_weeks
        color_print('yellow', "\nLet's compare the distances you have cycled on a week to week basis!")

        logged_weeks = {line['week'] for line in self.data}
        print('You have logged trips from these weeks:')
        for i in logged_weeks:
            color_print('green', i)

        running = True
        while running:
            num_of_weeks = input('\nHow many weeks do you want to compare? ')
            if not num_of_weeks.isdigit():
                color_print('red', f'Please choose an integer value between 1 and {len(logged_weeks)}.')
            else:
                num_of_weeks = int(num_of_weeks)
                if 0 < num_of_weeks <= len(logged_weeks):
                    running = False
                elif num_of_weeks > len(logged_weeks):
                    color_print('red', f'You have only saved trips from {len(logged_weeks)} weeks.')
                elif num_of_weeks <= 0:
                    color_print('red', 'You have to choose at least one week.')

        week_numbers = {}
        for i in range(num_of_weeks):
            week_numbers[i] = int(input(f'Type week {i + 1}: '))

        week_distances = {}  # Comprehension?
        for i in week_numbers.values():
            week_distances[i] = self.calc_weekly_distance(i)

        weeks = week_distances.keys()
        distances = week_distances.values()
        self.bar_plot_distance(weeks, distances)
        input()

        week_durations = {}  # Comprehension?
        for i in week_numbers.values():
            week_durations[i] = self.calc_weekly_duration(i)

        weeks = week_durations.keys()
        durations = [(duration / 60) for duration in week_durations.values()]
        self.bar_plot_duration(weeks, durations)

        return weeks, distances, durations  # Should I return any value?

    @staticmethod
    def bar_plot_distance(weeks, distances):  # If the user chooses weeks with a gap in between,
        # the x axe will show the weeks in the gap.
        """
        The method is being called by compare_weeks().
        :param weeks: int
        :param distances: float
        :return: None
        """
        ax = plt.figure().gca()
        # ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.xaxis.get_major_locator().set_params(integer=True)

        plt.title('Bike Distance Bar Plot for Chosen Weeks')
        plt.xlabel('Weeks')
        plt.ylabel('Distance in km')
        plt.bar(weeks, distances)
        plt.show()

    @staticmethod
    def bar_plot_duration(weeks, durations):  # If the user chooses weeks with a gap in between,
        # the x axe will show the weeks in the gap.
        """
        The method is being called by compare_weeks().
        :param weeks: int
        :param durations: float
        :return: None
        """
        threshold = 150
        ax = plt.figure().gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.plot([0., 4.5], [threshold, threshold], "k--")

        xint = range(min(weeks), max(weeks) + 1)
        matplotlib.pyplot.xticks(xint)

        plt.title('Bike Trip Durations Bar Plot for Chosen Weeks')
        plt.xlabel('Weeks')
        plt.ylabel('Duration')
        plt.bar(weeks, durations)
        plt.show()
        """
          import numpy as np
          import matplotlib.pyplot as plt

          # some example data
          threshold = 43.0
          values = np.array([30., 87.3, 99.9, 3.33, 50.0])
          x = range(len(values))

          # split it up
          above_threshold = np.maximum(values - threshold, 0)
          below_threshold = np.minimum(values, threshold)

          # and plot it
          fig, ax = plt.subplots()
          ax.bar(x, below_threshold, 0.35, color="g")
          ax.bar(x, above_threshold, 0.35, color="r",
                  bottom=below_threshold)

          # horizontal line indicating the threshold
          ax.plot([0., 4.5], [threshold, threshold], "k--")

          fig.savefig("look-ma_a-threshold-plot.png")
          """

    def three_longest_trips(self):
        """
        Called by run() in presentation.py, case 3. Prints the three longest trips from a chosen loaded file.
        :return: None
        """
        # print('\nChoose a file to see the three longest trips.')
        # data = self.load_file()
        lengths = [self.m_to_km(line['distance']) for line in self.data]
        lengths.sort(reverse=True)

        color_print('magenta', '\nThese are the three longest trips you have made:')
        count = 1
        for i in lengths[:3]:
            print(f'{count}. {i:.3f} km')
            count += 1

    def saved_emissions(self):
        """
        Called by run() in presentation.py, case 3. Calculates and prints saved CO2 emissions made not going by car.
        :return: None
        """
        self.data = self.load_file()  # Set the file in self
        emissions = 0

        for line in self.data:
            emissions += round((self.m_to_km(line['distance'] * 0.12)), 2)

        color_print('cyan', f'\nBy making all your trips by bike you have saved {emissions} kg CO2 equivalents!')
        return emissions

    @staticmethod
    def m_to_km(meter):
        km = meter / 1000
        return km

    @staticmethod
    def load_file():
        """
        Called by calc_weekly_distance(), saved_emissions() and three_longest_trips. Loads file from ./saved_trips.
        :return: data (json)
        """
        trips = Trips()
        saved_trips = trips.saved_trips()

        while True:
            file_name = input('Select the file you want to load: ')
            if file_name in saved_trips:
                file_name += '.json'
                with open('./saved_trips/' + file_name, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                break
            else:
                print('Could not find a file with that name, please try again.')

        return data

    """
    20% lower risk for premature death with 150 minutes of physical activity/week on a least moderate level.
    """
