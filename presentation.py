from terminal_color import color_print
from trips import Trips
from travel import Travel


class Presentation:
    def __init__(self):
        pass  # Do I need to instantiate an object here with variables?

    @staticmethod
    def run():
        color_print('cyan', "Welcome to WHAT´S __INIT__ FOR ME!")
        color_print('cyan', 'Here you can compare the estimated times for travelling from a to b going by bike and car.')
        color_print('cyan', 'You can also log your bike trips and see statistics.')
        running = True

        while running:
            # I will later add more alternatives to see statistics.
            color_print('green', '\nPlease choose between following alternatives:')
            color_print('green', 'Press [1] to comparing travel time.')
            color_print('green', 'Press [2] to log a bike trip.')
            color_print('green', 'Press [3] to quit.')
            user_input = input('Now make your choice: ')
            match user_input:
                case "1":
                    pass
                    # Here I want to call travel_questions, compare_bike_and_car etc but I can not figure out how.
                case "2":
                    pass
                    # And here I will call log_trip but have the same problem.
                case "3":
                    color_print('cyan', 'Thank you for visiting us. Have a nice day and welcome back!')
                    running = False
                case _:
                    color_print('red', 'Please choose between the alternatives.')

