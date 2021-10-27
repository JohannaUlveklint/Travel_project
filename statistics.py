import json
import datetime
from decimal import Decimal
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from terminal_color import color_print


class Statistics:
    def __init__(self):
        pass
    
    def calc_distance(self):
        with open('./saved_trips/test_statistics.wifm', 'r', encoding='utf-8') as json_file:
            # Change file later in all methods so that the user chooses which file to get data from
            data = json.load(json_file)
            meter = 0
            for line in data:
                meter += line['distance']
            distance = self.m_to_km(meter)
        return distance
    
    def calc_weekly_distance(self, week):
        with open('./saved_trips/test_statistics.wifm', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            meter = 0
            distance = 0  # Do I really need to declare distance here?
    
            for line in data:
                if line['week'] == week:
                    meter += line['distance']
                    distance = self.m_to_km(meter)
                # if not all line['week'] == week:  # How do I check if logs from a certain week is missing?
                #     print(f'There are no logged/saved trips from week {week}.')
                #     break

                # Nested loop to sort by year and week (and month), datetime?
    
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
        # the x axe will show the weeks in between.
        ax = plt.figure().gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.title('Bike Distance Bar Plot for Chosen Weeks')
        plt.xlabel('Weeks')
        plt.ylabel('Distance in km')
        plt.bar(weeks, distances)
        plt.show()
    
    def calc_duration(self):
        with open('./saved_trips/test_statistics.wifm', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            seconds = 0  # Comprehension
            for line in data:
                seconds += line['duration']
            duration = self.sec_converter(seconds)
        return duration

    def three_longest_trips(self):
        with open('./saved_trips/test_statistics.wifm', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            lengths = [self.m_to_km(line['distance']) for line in data]
            lengths.sort(reverse=True)
            color_print('yellow', '\nThese are the three longest trips you have made:')
            count = 1
            for i in lengths[:3]:
                print(f'{count}. {i} km')
                count += 1

    def saved_emissions(self):
        with open('./saved_trips/test_statistics.wifm', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
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
    
    
def main():
    statistics = Statistics()
    print(statistics.calc_distance())
    statistics.three_longest_trips()

    # week, distance = statistics.calc_weekly_distance(18)
    # print(f'Distance week {week}: {distance} km!')

    # print(week_distance)  # {18: Decimal('39.693'), 19: Decimal('39.893')}




if __name__ == '__main__':
    main()
