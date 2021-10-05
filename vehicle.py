class Vehicle:
    def __init__(self, user_vehicle=None, speed=0, to_vehicle=0, to_end_destination=0):
        self.user_vehicle = user_vehicle
        self.speed = speed
        self.to_vehicle = to_vehicle
        self.to_end_destination = to_end_destination

    def to_and_from_vehicle(self, to_vehicle, to_end_destination):
        walking_time = to_vehicle + to_end_destination
        return walking_time

    def travel_questions(self, user_vehicle):

        distance = int(input('How long is the distance you want to travel? Please answer in km. '))
        to_vehicle = int(input(f'How many minutes walk is it to your {user_vehicle}? '))
        to_end_destination = int(input('How many minutes walk is it to your end destination? '))
        return distance, to_vehicle, to_end_destination
