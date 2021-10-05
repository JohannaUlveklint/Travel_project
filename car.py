from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, user_vehicle='car', speed=50, buy_ticket_time=2, to_vehicle=0, to_end_destination=0):
        self.speed = speed
        self.user_vehicle = user_vehicle
        self.buy_ticket_time = buy_ticket_time
        self.to_vehicle = to_vehicle
        self.to_end_destination = to_end_destination

    def time_by_car(self, speed, distance, walking_time, buy_ticket_time):
        print('The expected average speed including stopping for traffic lights will be 50 km/h.')
        time = (distance / speed) * 60 + walking_time + buy_ticket_time
        return time
