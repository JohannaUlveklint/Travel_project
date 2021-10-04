import Vehicle
import Bike
import Car


def travel_questions(self):
    while user_vehicle != 'bike' and user_vehicle != 'car':
        user_vehicle = input("Do you want to go by [b]ike or [c]ar? ")
        if user_vehicle.lower() == 'b':
            self.user_vehicle = 'bike'
            print('You chose the bike.')
        elif user_vehicle.lower() == 'c':
            self.user_vehicle = 'car'
            print('You chose the car.')
        else:
            print('Please choose "b" for bike or "c" for car.')
    distance = int(input('How long is the distance you want to travel? Please answer in km. '))
    to_vehicle = int(input(f'How many minutes walk is it to your {user_vehicle}? '))
    to_end_destination = int(input('How many minutes walk is it to your end destination? '))
    return self.user_vehicle, distance, to_vehicle, to_end_destination


def total_time(self, user_vehicle, walking_time, distance):
    if user_vehicle == 'bike':
        print(f'Your total travel time is estimated to {time_by_bike(distance, walking_time)} minutes.')
    if user_vehicle == 'car':
        print(f'Your total travel time is estimated to {time_by_car(distance, walking_time)} minutes.')


def main():
    # Trying to get local variables inside functions with self.
    user_vehicle = None
    travel_questions()
    if user_vehicle == 'bike':
        vehicle = Bike()
        print(user_vehicle)
    elif user_vehicle == 'car':
        vehicle = Car()
        print(user_vehicle)
    else:
        print('Something got wrong')


if __name__ == '__main__':
    main()
