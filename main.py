from travel import Travel


def main():
    traveller1 = Travel()
    traveller1.travel_questions()
    traveller2 = Travel()
    traveller2.travel_questions()
    traveller1.time_by_car()  # The data is stored in the traveller obj and don´t have to be passed
    traveller1.time_by_bike()
    traveller2.time_by_car()  # The data is stored in the traveller obj and don´t have to be passed
    traveller2.time_by_bike()


if __name__ == '__main__':
    main()
