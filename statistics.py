import json
import datetime
from decimal import Decimal
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


class Statistics:
    def __init__(self):
        pass
    
    def calc_distance(self):
        with open('./saved_trips/test_statistics.wifm', 'r', encoding='utf-8') as json_file:
            # Change file later so that the user chooses which file to get data from
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
    """
    var={}
    var[1] = 10
    var[2] = 100
    var[3] = 1000
    
    test={}
    for i in range(1,4):
        test[i] = var[i] +1
    
    print(test)
    """
    def compare_weeks(self):
        num_of_weeks = int(input('How many weeks do you want to compare? '))
        week_numbers = {}
        for i in range(num_of_weeks):
            week_numbers[i] = int(input(f'Type week {i + 1}: '))

        week_distances = {}
        for i in week_numbers.values():
            week_distances[i] = self.calc_weekly_distance(i)[1]
        weeks = week_distances.keys()
        distances = week_distances.values()
        return weeks, distances

    def bar_plot(self, weeks, distances):
        ax = plt.figure().gca()
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.title('Bike Distance Bar Plot for Chosen Weeks')
        plt.xlabel('Weeks')
        plt.ylabel('Distance in km')
        plt.bar(weeks, distances)
        plt.show()

    def m_to_km(self, meter):
            km = Decimal(meter / 1000).quantize(Decimal("1.000"))
            return km
    
    # def m_to_mil(self, meter):
    #         mil = Decimal(meter / 10000).quantize(Decimal("1.000"))
    #         return mil
    
    def calc_duration(self):
        with open('./saved_trips/test_statistics.wifm', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            seconds = 0
            for line in data:
                seconds += line['duration']
            duration = self.sec_converter(seconds)
        return duration
    
    def sec_converter(self, time_in_sec):
        time = datetime.timedelta(seconds=time_in_sec)
        time_without_ms = time - datetime.timedelta(microseconds=time.microseconds)
        return time_without_ms
    
    
def main():
    statistics = Statistics()
    print(statistics.calc_distance())
    # week, distance = statistics.calc_weekly_distance(18)
    # print(f'Distance week {week}: {distance} km!')

    weeks, distances = statistics.compare_weeks()  # Returns lists weeks and distances
    statistics.bar_plot(weeks, distances)
    # print(week_distance)  # {18: Decimal('39.693'), 19: Decimal('39.893')}


    # print(weeks)  # dict_keys([18, 19])
    # print(distances)  # dict_values([Decimal('39.693'), Decimal('39.893')])
    #
    # for week in weeks:
    #     print(week)
    #
    # for distance in distances:
    #     print(distance)



if __name__ == '__main__':
    main()
