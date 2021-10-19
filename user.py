import json
from os import listdir

from terminal_color import color_print
from travel import Travel
from trips import Trips
from presentation import Presentation
from address import Address


class User:
    def __init__(self):
        self.travel = Travel()
        self.trips = Trips()
        self.presentation = Presentation()
        self.address = Address()

    def save_to_json(self, trips):
        file_name = input("Please choose a name to save your logged trips with: ")
        file_name += '.wifm'
        with open('./saved_trips/' + file_name, 'w', encoding='utf-8') as json_file:
            json.dump(trips, json_file)  # Dumps save trips to a file

    @staticmethod
    def list_saved_trips():
        files = []
        for f in listdir('./saved_trips'):
            if f.endswith('.wifm'):
                files.append(f.replace('.wifm', ''))

        files = [f.replace('.wifm', '') for f in listdir('./saved_trips') if f.endswith('.wifm')]

        return files

    def load_from_json(self):
        saved_trips = self.list_saved_trips()

        while True:
            print("Saved trips:")
            for trip in saved_trips:
                color_print("yellow", f"\t{trip}")
            file_name = input("Please choose a saving to load: ")
            if file_name in saved_trips:
                break
            color_print("red", f"The name '{file_name}' does not corresponds to any save, please try again.")

        file_name += '.wifm'
        with open('./saved_trips/' + file_name, 'r', encoding='utf-8') as json_file:
            return json.load(json_file), file_name


def main():
    trips = [
        {
            'start_point': 'A',
            'end_point': 'B',
            'distance': 345
        },
        {
            'start_point': 'C',
            'end_point': 'D',
            'distance': 234
        },
        {
            'start_point': 'E',
            'end_point': 'F',
            'distance': 123
        },
        {
            'start_point': 'G',
            'end_point': 'H',
            'distance': 456
        },
    ]

    user = User()
    # If the user chooses to load a save
    loaded, file_name = user.load_from_json()
    print('These are the saved trips:')
    for row in loaded:
        print( row)

    choice = input(f'Do you want to log more trips to {file_name[:-5]}? y/n: ')
    while choice.lower() != 'y' and choice.lower() != 'n':
        choice = input('Please type "y" for yes or "n" for no: ')


if __name__ == '__main__':
    main()
