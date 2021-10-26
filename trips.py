import json
import os
from os import listdir

from terminal_color import color_print
import datetime
from travel import Travel


class Trips:
    def __init__(self):
        self.logged_trips = []
        self.travel = Travel()

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
        cd, rbd, ebd, cdu, rbdu, ebdu = self.travel.get_distance_and_duration()

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
        while True:
            if bike_type.lower() == 'r':
                # distance, duration = travel.get_distance_and_duration()[1][4]
                distance, duration = rbd, rbdu
                break
            elif bike_type.lower() == 'e':
                # distance, duration = travel.get_distance_and_duration()[2][5]
                distance, duration = ebd, ebdu
                break
            else:
                color_print('red', 'Please choose [r] for regular or [e] for electric.')

        trip = {'year': year, 'month': month, 'day': day, 'week': week, 'distance': distance, 'duration': duration}  # Add emissions?
        # self.logged_trips.append(trip)
        # print(self.logged_trips[0])
        self.save_to_json(trip)
        # return self.logged_trips

    def save_to_json(self, new_trip):
        # self.logged_trips.append(new_trip)  # Skip?
        # saved_trips = []

        saved_trips = self.list_saved_trips()
        print("Saved trips:")
        if len(saved_trips) == 0:
            print('There is no saved trips')
        else:
            for trip in saved_trips:
                color_print("yellow", f"\t{trip}")
        file_name = input("Save your trip to an existing saved file or choose a new name: ")
        # file_name += '.json'

        if file_name in saved_trips:
            with open('./saved_trips/' + file_name, 'r', newline='\n', encoding='utf-8') as file:  # No new line
                data = json.load(file)
            data.append(new_trip)

            with open('./saved_trips/' + file_name, 'w', encoding='utf-8') as file:  # , newline='\n'
                json.dump(data, file)
            print(new_trip)

        else:
            data = self.logged_trips
            # saved_trips.append(new_trip)
            data.append(new_trip)
            with open('./saved_trips/' + file_name, 'w', encoding='utf-8') as file:  # , newline='\n'
                json.dump(data, file)  # Dumps save trips to a file

        """

                  https://blog.finxter.com/how-to-append-data-to-a-json-file-in-python/
                  filename = 'your_file.json'
                  entry = {'carl': 33}
                  # 1. Read file contents
                  with open(filename, "r") as file:
                      data = json.load(file)
                  # 2. Update json object
                  data.append(entry)
                  # 3. Write json file
                  with open(filename, "w") as file:
                      json.dump(data, file)
                  """

    def load_from_json(self, file_name):
        # saved_trips = self.list_saved_trips()

        # while True:
        #     print("Saved trips:")
        #     for trip in saved_trips:
        #         color_print("yellow", f"\t{trip}")
        #     file_name = input("Please choose a saving to load: ")
        #     if file_name in saved_trips:
        #         break
        #     color_print("red", f"The name '{file_name}' does not corresponds to any save, please try again.")

        # file_name += '.json'
        with open('./saved_trips/' + file_name, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

    @staticmethod
    def list_saved_trips():
        # files = []
        # for f in listdir('./saved_trips'):
        #     if f.endswith('.json'):
        #         files.append(f.replace('.json', ''))

        # files = [f.replace('.json', '') for f in listdir('./saved_trips') if f.endswith('.json')]
        files = [f for f in listdir('./saved_trips') if f.endswith('.json')]

        return files

    def print_trip(self):
        pass

    def get_weekly_training_data(self):
        pass



