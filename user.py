import json
from os import listdir

from terminal_color import color_print
from travel import Travel
from trips import Trips
from presentation import Presentation


class User:
    def __init__(self):
        self.travel = Travel()
        self.trips = Trips()
        self.presentation = Presentation()




def main():
    pass
    # user = User()
    # # If the user chooses to load a save
    # loaded, file_name = user.load_from_json()
    # print('These are the saved trips:')
    # for row in loaded:
    #     print( row)
    #
    # choice = input(f'Do you want to log more trips to {file_name[:-5]}? y/n: ')
    # while choice.lower() != 'y' and choice.lower() != 'n':
    #     choice = input('Please type "y" for yes or "n" for no: ')
    #
    # trips = [
    #     {
    #         'start_point': 'A',
    #         'end_point': 'B',
    #         'distance': 345
    #     },
    #     {
    #         'start_point': 'C',
    #         'end_point': 'D',
    #         'distance': 234
    #     },
    #     {
    #         'start_point': 'E',
    #         'end_point': 'F',
    #         'distance': 123
    #     },
    #     {
    #         'start_point': 'G',
    #         'end_point': 'H',
    #         'distance': 456
    #     },
    # ]
    #

if __name__ == '__main__':
    main()
