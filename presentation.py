from terminal_color import color_print
from travel import Travel
from trips import Trips
from statistics import Statistics


class Presentation:
    def __init__(self):
        pass

    @staticmethod
    def run():
        color_print('cyan', '\033[1m' + "Welcome to WHAT´S __INIT__ FOR ME!")
        color_print('cyan', 'Here you can compare the estimated times for travelling from a to b going by bike and car.')
        color_print('cyan', 'You can also log your bike trips and see statistics.')
        running = True

        while running:
            color_print('green', '\nPlease choose between following alternatives:')
            color_print('green', 'Press [1] to comparing travel time.')
            color_print('green', 'Press [2] to save a bike trip.')
            color_print('green', 'Press [3] to see statistics for your saved bike trips.')
            color_print('green', 'Press [4] to print saved trips')
            color_print('green', 'Press [5] to quit.')
            user_input = input('What do you want to do? ')

            travel = Travel()  # Have these in __init__?
            trips = Trips()
            statistics = Statistics()

            match user_input:
                case "1":
                    travel.print_route_data()
                    input()
                case "2":
                    trips.log_trip()
                    input()
                case "3":
                    statistics.saved_emissions()
                    statistics.three_longest_trips()
                    input()
                    statistics.compare_weeks()
                    input()
                case "4":
                    trips.print_trips()
                    input()
                case "5":
                    color_print('cyan', 'Thank you for visiting us. Have a nice day and welcome back!')
                    running = False
                case _:
                    color_print('red', 'Please choose between the alternatives.')

