from vehicle import Vehicle
from bike import Bike
from car import Car

# def total_time(self, user_vehicle, walking_time, distance):
#     if user_vehicle == 'bike':
#         print(f'Your total travel time is estimated to {time_by_bike(distance, walking_time)} minutes.')
#     if user_vehicle == 'car':
#         print(f'Your total travel time is estimated to {time_by_car(distance, walking_time)} minutes.')
#


def main():
    # Get rid of all the variables below
    user_vehicle, cycling_style = None, None
    to_vehicle, to_end_destination, distance, walking_time, changing_time, buy_ticket_time, speed, time = \
        0, 0, 0, 0, 0, 0, 0, 0
    while user_vehicle != 'bike' and user_vehicle != 'car':
        user_vehicle = input("Do you want to go by [b]ike or [c]ar? ")
        if user_vehicle.lower() == 'b':
            user_vehicle = 'bike'
            vehicle = Bike()
            print('You chose the bike.')
        elif user_vehicle.lower() == 'c':
            user_vehicle = 'car'
            vehicle = Car
            print('You chose the car.')
        else:
            print('Please choose "b" for bike or "c" for car.')

    # How to put this as functions in classes?
    vehicle.travel_questions(user_vehicle)
    vehicle.to_and_from_vehicle(to_vehicle, to_end_destination)
    if user_vehicle == 'bike':
        vehicle.time_by_bike(distance, walking_time, cycling_style, changing_time)
    elif user_vehicle == 'car':
        vehicle.time_by_car(speed, distance, walking_time, buy_ticket_time)
    print(f'The estimated total travel time for your journey is {time} minutes.')


if __name__ == '__main__':
    main()
