import json
from os import listdir

from terminal_color import color_print
import datetime
from travel import Travel


class Trips:
    def __init__(self):
        self.logged_trips = []
        self.travel = Travel()

    @staticmethod
    def __get_user_input(question):
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
        cd, rbd, ebd, cdu, rbdu, ebdu, map_url = self.travel.get_distance_and_duration()

        while running:
            year = self.__get_user_input('\nEnter year with four digits: ')
            month = self.__get_user_input('Enter the number of the month with one or two digits: ')
            day = self.__get_user_input('Enter day with one or two digits: ')
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

        bike_type = input('Are you riding a [r]egular or [e]lectric bike? Choose [e] if you are a fast biker.')
        while True:
            if bike_type.lower() == 'r':
                distance, duration = rbd, rbdu
                break
            elif bike_type.lower() == 'e':
                distance, duration = ebd, ebdu
                break
            else:
                color_print('red', 'Please choose [r] for regular or [e] for electric.')

        trip = {'year': year, 'month': month, 'day': day, 'week': week, 'distance': distance, 'duration': duration}
        self.save_to_json(trip)

    @staticmethod
    def saved_trips():
        saved_trips = [f.replace('.json', '') for f in listdir('./saved_trips') if f.endswith('.json')]
        print("Saved trips:")
        if len(saved_trips) == 0:
            print('There is no saved trips')
        else:
            for trip in saved_trips:
                color_print("yellow", f"\t{trip}")
        return saved_trips

    def save_to_json(self, new_trip):
        saved_trips = self.saved_trips()
        file_name = input("Save your trip to an existing saved file or choose a new name: ")

        if file_name in saved_trips:
            file_name += '.json'
            with open('./saved_trips/' + file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
            data.append(new_trip)
            with open('./saved_trips/' + file_name, 'w', encoding='utf-8') as file:
                json.dump(data, file)
        else:
            file_name += '.json'
            data = self.logged_trips
            data.append(new_trip)
            with open('./saved_trips/' + file_name, 'w', encoding='utf-8') as file:
                json.dump(data, file)

        color_print('yellow', 'Your trip is saved!')

    def print_trip(self):
        saved_trips = self.saved_trips()
        file_name = input('Choose a saved file to print: ')
        if file_name in saved_trips:
            file_name += '.json'
            with open('./saved_trips/' + file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)

        # Sort function for year, month and day before printing?

        total_distance = 0
        print('====================')
        for line in data:
            total_distance += self.travel.m_to_km(line['distance'])
            print(f"Date: {line['year']}-{line['month']}-{line['day']}")
            print(f"Distance: {self.travel.m_to_km(line['distance']):.3f} km")
            print(f"Duration: {self.travel.sec_converter(line['duration'])}\n")
        print(f'Totally, you have gone {total_distance:.3f} km by bike, great work!')
        print('======================================================')


def main():
    trip = Trips()
    trip.print_trip()


if __name__ == '__main__':
    main()
