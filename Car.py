import Vehicle


class Car(Vehicle):
    def __init__(self, speed=50, buy_ticket_time=2):
        self.speed = speed
        self.buy_ticket_time = buy_ticket_time

    def time_by_car(self, speed, distance, walking_time, buy_ticket_time):
        print('The expected average speed including stopping for traffic lights will be 50 km/h.')
        time = (distance / speed) * 60 + walking_time + buy_ticket_time
        return time
