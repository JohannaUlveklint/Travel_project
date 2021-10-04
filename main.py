user_vehicle = None
distance, to_vehicle, to_end_destination, walking_time = 0, 0, 0, 0

def travel_questions():
    while user_vehicle != 'bike' and user_vehicle != 'car':
        user_vehicle = input("Do you want to go by [b]ike or [c]ar? ")
        if user_vehicle.lower() == 'b':
            user_vehicle = 'bike'
            print('You chose the bike.')
        elif user_vehicle.lower() == 'c':
            user_vehicle = 'car'
            print('You chose the car.')
        else:
            print('Please choose "b" for bike or "c" for car.')
    distance = int(input('How long is the distance you want to travel? Please answer in km. '))
    to_vehicle = int(input(f'How many minutes walk is it to your {user_vehicle}? '))
    to_end_destination = int(input('How many minutes walk is it to your end destination? '))
    return user_vehicle, distance, to_vehicle, to_end_destination


def time_by_bike(distance, walking_time):
    cycling_style = None
    cycling_speed = 0
    changing_time = 0
    while cycling_style != 'moderate' and cycling_style != 'fast':
        cycling_style = input('Do you consider yourself a [m]oderate or [f]ast cyclist? ')
        if cycling_style == 'm':
            cycling_style = 'moderate'
            cycling_speed = 15
            print('The expected average speed including stopping for traffic lights will be 15 km/h.')
        elif cycling_style == 'f':
            cycling_style = 'fast'
            cycling_speed = 20
            changing_time = 5
            print('The expected average speed including stopping for traffic lights will be 20 km/h.')
            print('Five minutes for changing training clothes will be included.')
        else:
            print('Please choose "m" for moderate cyclist or "f" for fast cyclist.')
    time = (distance / cycling_speed) * 60 + walking_time + changing_time
    return time


def time_by_car(distance, walking_time):
    print('The expected average speed including stopping for traffic lights will be 50 km/h.')
    buy_ticket_time = 2
    time = (distance / 50) * 60 + walking_time + buy_ticket_time
    return time


def to_and_from_vehicle(to_vehicle, to_end_destination):
    walking_time = to_vehicle + to_end_destination
    return walking_time


def total_time(user_vehicle, walking_time, distance):
    if user_vehicle == 'bike':
        print(f'Your total travel time is estimated to {time_by_bike(distance, walking_time)} minutes.')
    if user_vehicle == 'car':
        print(f'Your total travel time is estimated to {time_by_car(distance, walking_time)} minutes.')


def run():
    # travel_questions()
    to_and_from_vehicle(to_vehicle, to_end_destination)
    total_time(user_vehicle, walking_time, distance)


def main():
    # Maybe I first should call travel_questions(), then make classes, instantiate an object and then call run()
    run()


if __name__ == '__main__':
    main()
