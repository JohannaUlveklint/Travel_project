import json
import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from trips import Trips
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
        """
        The method is being called by compare_weeks().
        :param week: int
        :return:
        """
        data = self.load_file()
        meter = 0
        distance = 0

        for line in data:
            if week in data.values() is False:
                print('No trips for that week has been saved.')
                break
            if line['week'] == week:
                meter += line['distance']
                distance = self.m_to_km(meter)

        return distance

    def compare_weeks(self):
        """
        Called by run() in presentation.py, case 3. Compares the total distance made by bike each chosen week and shows
        the result in a bar plot.
        :return: ?
        """
        color_print('yellow', "\nLet's compare the distances you have cycled on a week to week basis!")
        num_of_weeks = int(input('How many weeks do you want to compare? '))
        week_numbers = {}
        for i in range(num_of_weeks):
            week_numbers[i] = int(input(f'Type week {i + 1}: '))

        week_distances = {}  # Comprehension?
        for i in week_numbers.values():
            week_distances[i] = self.calc_weekly_distance(i)

        weeks = week_distances.keys()
        distances = week_distances.values()
        self.bar_plot(weeks, distances)
        return weeks, distances  # Should I return any value?

    @staticmethod
    def bar_plot(weeks, distances):  # If the user chooses weeks with a gap in between,
        # the x axe will show the weeks in the gap.
        """
        The method is being called by compare_weeks().
        :param weeks: int
        :param distances: float
        :return: None
        """
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
        """
        Called by run() in presentation.py, case 3. Prints the three longest trips from a chosen loaded file.
        :return: None
        """
        data = self.load_file()
        lengths = [self.m_to_km(line['distance']) for line in data]
        lengths.sort(reverse=True)

        color_print('yellow', '\nThese are the three longest trips you have made:')
        count = 1
        for i in lengths[:3]:
            print(f'{count}. {i:.3f} km')
            count += 1

    def saved_emissions(self):
        """
        Called by run() in presentation.py, case 3. Calculates and prints saved CO2 emissions made not going by car.
        :return: None
        """
        data = self.load_file()
        emissions = 0

        for line in data:
            emissions += round((self.m_to_km(line['distance'] * 0.12)), 2)

        color_print('yellow', f'\nBy making all your trips by bike you have saved {emissions} kg CO2 equivalents!')

    @staticmethod
    def m_to_km(meter):
        km = meter / 1000
        return km

    # @staticmethod
    # def sec_converter(time_in_sec):
    #     time = datetime.timedelta(seconds=time_in_sec)
    #     time_without_ms = time - datetime.timedelta(microseconds=time.microseconds)
    #     return time_without_ms

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
    Aerob fysisk aktivitet enligt rådande rekommendationer: Regelbunden aerob fysisk
    aktivitet (150 minuter per vecka med minst måttlig intensitet) påverkar
    skelettmuskulatur, hjärta, blodkärl och kroppssammansättning positivt, och har i
    metaanalyser visat sig vara förenat med cirka 20 procent lägre risk för förtida död. 
    Jämfört med att sitta stilla 
    """
