import json
import datetime
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
# import seaborn as sns

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
        seconds = 0

        for line in self.data:
            if line['week'] == week:
                seconds += line['duration']

        return seconds

    def compare_weeks(self):  # Split up!
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
            running = True
            while running:
                week_input = input(f'Type week {i + 1}: ')
                if week_input.isdigit():
                    if int(week_input) in logged_weeks:
                        week_numbers[i] = int(week_input)
                        running = False
                    else:
                        print('You have logged trips from these weeks:')
                        for week in logged_weeks:
                            color_print('green', week)
                        print('Try again.')
                else:
                    print('Please enter a valid number.')

        week_distances = {}  # Comprehension?
        for i in week_numbers.values():
            week_distances[i] = self.calc_weekly_distance(i)

        weeks = week_distances.keys()
        distances = week_distances.values()
        color_print('yellow', "Let's check how far you have gone!")
        input()
        self.bar_plot_distance(weeks, distances)
        input()

        week_durations = {}  # Comprehension?
        for i in week_numbers.values():
            week_durations[i] = self.calc_weekly_duration(i)

        weeks = week_durations.keys()
        durations = [(duration / 60) for duration in week_durations.values()]
        color_print('blue', 'WHO recommends a minimum of 150 minutes physical activity/week on a moderate level or higher.')
        color_print('blue', 'Do you think your bike trips helped you towards that recommendation?')
        input()
        self.bar_plot_duration(weeks, durations)

        # if min(lst) > a and max(lst) < b:
        if max(durations) <= 30:
            color_print('magenta', 'All trips made by bike are better than not taking the bike at all!')
        elif min(durations) > 30 and max(durations) < 100:
            color_print('magenta', 'This is a good start. Just choose the bike a little more often and you are there!')
        elif min(durations) >= 100 and max(durations) < 150:
            color_print('magenta', 'So close! It is just a small extra effort and you will reach the line!')
        elif min(durations) >= 150:
            color_print('magenta', "You've nailed it!")
        if max(durations) > 300:
            color_print('magenta', 'Look at that week: 2 * WHO!')
        if max(durations) > 600:
            color_print('magenta', 'Just like Armstrong, only not on steroids.')
        input()
        color_print('cyan', "Let's look att your distance vs duration!")
        input()
        self.scatter_plot()


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
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        # ax.xaxis.get_major_locator().set_params(integer=True)

        plt.title('Bike Distance Bar Plot for Chosen Weeks')
        plt.xlabel('Weeks')
        plt.ylabel('Distance in km')
        plt.bar(weeks, distances)
        plt.show()

    def bar_plot_duration(self, weeks, durations):  # If the user chooses weeks with a gap in between,
        # the x axe will show the weeks in the gap.
        """
        The method is being called by compare_weeks().
        :param weeks: int
        :param durations: float
        :return: None
        """
        # durations = [(int(line['duration']) / 60) for line in self.data]
        threshold = 150
        ax = plt.figure().gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.xlim((min(weeks))-0.5, (max(weeks))+0.5)

        # If I want to continue working on separate colors below and above threshold:
        # x = range(len(durations))
        # above_threshold = np.maximum(max(durations) - threshold, 0)
        # below_threshold = np.minimum(min(durations), threshold)
        #
        # fig, ax = plt.subplots()
        # ax.bar(x, below_threshold, 0.35, color="g")
        # ax.bar(x, above_threshold, 0.35, color="r", bottom=below_threshold)
        ax.plot([(min(weeks))-0.5, (max(weeks))+0.5], [threshold, threshold], "k--")

        plt.title('Bike Trip Durations Bar Plot for Chosen Weeks')
        plt.xlabel('Weeks')
        plt.ylabel('Duration in minutes')
        plt.bar(weeks, durations)
        plt.show()
        """
          https://stackoverflow.com/questions/28129606/how-to-create-a-matplotlib-bar-chart-with-a-threshold-line
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
    def scatter_plot(self):
        distances = [(int(line['distance']) / 1000) for line in self.data]
        durations = [(int(line['duration']) / 60) for line in self.data]

        plt.title('Distance vs Duration')
        plt.xlabel('Distance in km')
        plt.ylabel('Duration in min')
        plt.scatter(distances, durations, color='green')
        plt.show()

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

        color_print('cyan', f'\nBy making all your trips by bike you have saved {round(emissions, 2)} kg CO2 equivalents!')
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
