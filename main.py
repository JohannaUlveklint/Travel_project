from user import User


def main():
    # travel = Travel()
    # travel.travel_questions() This works since travel is an object of the class Travel.
    # travel.logged_trips() This does not work since logged_trips() is in another class
    user = User()
    # user.travel.travel_questions()  # Function is in right class
    # user.travel.time_by_car()  # The data is stored in the traveller obj and don´t have to be passed
    # user.travel.time_by_bike()
    user.trips.log_trip()
    for trip in user.trips.logged_trips:
        print(trip)


if __name__ == '__main__':
    main()
