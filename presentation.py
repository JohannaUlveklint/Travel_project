from terminal_color import color_print
from travel import Travel
from trips import Trips


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
            # I will later add more alternatives to see statistics.
            color_print('green', '\nPlease choose between following alternatives:')
            color_print('green', 'Press [1] to comparing travel time.')
            color_print('green', 'Press [2] to save a bike trip.')
            color_print('green', 'Press [3] to ?.')
            color_print('green', 'Press [4] to print saved trips')
            color_print('green', 'Press [5] to quit.')
            user_input = input('Now make your choice: ')

            travel = Travel()  # Have these in __init__?
            trips = Trips()

            match user_input:
                case "1":
                    travel.print_distance_and_duration()
                case "2":
                    trips.log_trip()
                case "3":
                    pass
                case "4":
                    trips.load_from_json()
                case "5":
                    color_print('cyan', 'Thank you for visiting us. Have a nice day and welcome back!')
                    running = False
                case _:
                    color_print('red', 'Please choose between the alternatives.')

