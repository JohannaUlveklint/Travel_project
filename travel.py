from terminal_color import color_print

class Travel:
    def __init__(self):
        self.distance = 0
        self.walking_time = 0

    def travel_questions(self):
        # The function does not have to return a value since it´s stored in self.distance and self.walking_time
        print()
        self.distance = int(input('How long is the distance you want to travel? Please answer in km. '))
        to_vehicle = int(input(f'How many minutes walk is it to your car or bike? '))
        to_end_destination = int(input('When you have parked your vehicle, '
                                       'how many minutes walk is it to your end destination? '))
        self.walking_time = to_vehicle + to_end_destination

    def time_by_car(self):
        color_print('green', '\nWe start by calculating the travel time if you go by car.')
        color_print('yellow', 'The expected average speed including stopping for traffic lights will be 50 km/h.')
        color_print('yellow', 'Five minutes for looking for a parking lot will be added to the total time.')
        speed = 50
        look_for_parking_time = 5
        time = (self.distance / speed) * 60 + self.walking_time + look_for_parking_time
        color_print('magenta', f'If you go this distance by car the total estimated travel time is {time} minutes.')
        return time

    def time_by_bike(self):
        color_print('green', '\nNow we are going to calculate the travel time if you go by bike.')
        color_print('green', 'But before we can do that we have a question for you:')
        cycling_style = None
        while cycling_style != 'moderate' and cycling_style != 'fast':
            cycling_style = input('Do you consider yourself a [m]oderate or [f]ast cyclist? ')
            if cycling_style == 'm':
                cycling_style = 'moderate'
                speed = 15
                changing_time = 0
                color_print('yellow', 'The expected average speed including stopping '
                                      'for traffic lights will be 15 km/h.')
            elif cycling_style == 'f':
                cycling_style = 'fast'
                speed = 20
                changing_time = 5
                color_print('yellow', 'The expected average speed including stopping '
                                      'for traffic lights will be 20 km/h.')
                color_print('yellow', 'Five minutes for change from training clothes will be included.')
            else:
                color_print('Please choose "m" for moderate tempo cyclist or "f" for fast cyclist.')
        time = (self.distance / speed) * 60 + self.walking_time + changing_time
        color_print('magenta', f'If you go this distance by bike the total estimated travel time is {time} minutes.')
        return time
