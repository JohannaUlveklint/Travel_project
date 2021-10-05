from vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self, speed=0, user_vehicle='bike', cycling_style=None, changing_time=0, to_vehicle=0, to_end_destination=0):
        self.speed = speed
        self.user_vehicle = user_vehicle
        self.cycling_style = cycling_style
        self.changing_time = changing_time
        self.to_vehicle = to_vehicle
        self.to_end_destination = to_end_destination

    def time_by_bike(self, distance, walking_time, cycling_style, changing_time):
        while cycling_style != 'moderate' and cycling_style != 'fast':
            cycling_style = input('Do you consider yourself a [m]oderate or [f]ast cyclist? ')
            if cycling_style == 'm':
                cycling_style = 'moderate'
                speed = 15
                print('The expected average speed including stopping for traffic lights will be 15 km/h.')
            elif cycling_style == 'f':
                cycling_style = 'fast'
                speed = 20
                changing_time = 5
                print('The expected average speed including stopping for traffic lights will be 20 km/h.')
                print('Five minutes for change from training clothes will be included.')
            else:
                print('Please choose "m" for moderate cyclist or "f" for fast cyclist.')
        time = (distance / speed) * 60 + walking_time + changing_time
        return time
