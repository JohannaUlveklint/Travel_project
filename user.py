from travel import Travel
from trips import Trips
from presentation import Presentation
from address import Address


class User:
    def __init__(self):
        self.travel = Travel()
        self.trips = Trips()
        self.presentation = Presentation()
        self.address = Address()
