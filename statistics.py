import json
import datetime
from decimal import Decimal
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from terminal_color import color_print


class Statistics:
    def __init__(self):
        pass
    
    # def calc_total_distance(self):
    #     data = self.load_file()
    #     meter = 0
    #     for line in data:
    #         meter += line['distance']
    #     distance = self.m_to_km(meter)
    #     return distance
    
    def calc_weekly_distance(self, week):
        data = self.load_file()
        meter = 0
        distance = 0

        for line in data:
            if line['week'] == week:
                meter += line['distance']
                distance = self.m_to_km(meter)
            # How do I check if logs from a certain week is missing?

        return week, distance

    def compare_weeks(self):
        color_print('yellow', "\nLet's compare the distances you have cycled on a week to week basis!")
        num_of_weeks = int(input('How many weeks do you want to compare? '))
        week_numbers = {}
        for i in range(num_of_weeks):
            week_numbers[i] = int(input(f'Type week {i + 1}: '))

        week_distances = {}
        for i in week_numbers.values():
            week_distances[i] = self.calc_weekly_distance(i)[1]
        weeks = week_distances.keys()
        distances = week_distances.values()
        self.bar_plot(weeks, distances)
        return weeks, distances

    @staticmethod
    def bar_plot(weeks, distances):  # If the user chooses weeks with a gap between,
        # the x axe will show the weeks in the gap.
        ax = plt.figure().gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.title('Bike Distance Bar Plot for Chosen Weeks')
        plt.xlabel('Weeks')
        plt.ylabel('Distance in km')
        plt.bar(weeks, distances)
        plt.show()
    
    # def calc_duration(self):
    #     data = self.load_file()
    #     seconds = 0
    #     for line in data:
    #         seconds += line['duration']
    #     duration = self.sec_converter(seconds)
    #     return duration

    def three_longest_trips(self):
        data = self.load_file()
        lengths = [self.m_to_km(line['distance']) for line in data]
        lengths.sort(reverse=True)
        color_print('yellow', '\nThese are the three longest trips you have made:')
        count = 1
        for i in lengths[:3]:
            print(f'{count}. {i} km')
            count += 1

    def saved_emissions(self):
        data = self.load_file()
        emissions = 0
        for line in data:
            emissions += round((self.m_to_km(line['distance'] * 0.12)), 2)
        color_print('yellow', f'\nBy making all your trips by bike you have saved {emissions} kg CO2 equivalents!')

    @staticmethod
    def m_to_km(meter):
        km = Decimal(meter / 1000).quantize(Decimal("1.000"))
        return km

    @staticmethod
    def sec_converter(time_in_sec):
        time = datetime.timedelta(seconds=time_in_sec)
        time_without_ms = time - datetime.timedelta(microseconds=time.microseconds)
        return time_without_ms

    @staticmethod
    def load_file():
        with open('saved_trips/test_statistics.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
