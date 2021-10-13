from travel import Travel
from trips import Trips


class User:
    def __init__(self):
        self.travel = Travel()
        self.trips = Trips()
