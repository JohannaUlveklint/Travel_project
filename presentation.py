from terminal_color import color_print


class Presentation:
    def __init__(self):
        pass

    @staticmethod
    def run(self):  # colorprint
        print('Welcome to Whats __init__ for me!')
        print('Here you can compare the estimated time for travel from a to b going by bike and car.')
        print('You can also log your bike trips and see statistics.')
        running = True

        while running:
            print('Please choose between following alternatives:')
            print('Press [1] to comparing travel time.')
            print('Press [2] to log a bike trip.')
            print('Press [3] to quit.')
            user_input = input('Now make your choice: ')
            match user_input:
                case 1:
                    user.travel.travel_questions()
                case 2:
                    user.trips.log_trip()
                case 3:
                    print('Thank you for visiting us. Have a nice day and welcome back!')
                    running = False
                case _:
                    print('Please choose between the alternatives.')

