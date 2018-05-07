# Hello world APP - Course Python Jumpstart
# Author: Victor Caldas

import datetime
from datetime import date


def print_header():
    print('--------------------------------')
    print('             BDAY APP')
    print('--------------------------------')
    print()


def get_bday_from_user():
    """

    :return: Ask the user for input
    """

    print('When were you born? ')

    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    print()

    birthday = datetime.date(year=year, month=month, day=day)

    return birthday


def compute_days_between_dates(birthday_date, today_date):
    """

    :param birthday_date: The older date, i.e Birthday
    :param today_date: The newer date, today
    :return: The difference in days
    """

    this_year: date = datetime.date(year=today_date.year, month=birthday_date.month, day=birthday_date.day)
    dt = this_year - today_date

    return dt.days


def print_bday_information(interval):
    """

    :param interval: The interval in days
    :return: Print the formated output
    """
    if interval > 0:
        print("Your birthday will be in {} days!".format(interval))
    elif interval < 0:
        print(f"Your birthday was {abs(interval)} days ago!")
    else:
        print("Happy Birthday!!!")


def main():
    print_header()

    birthday = get_bday_from_user()

    today = datetime.date.today()
    interval = compute_days_between_dates(birthday, today)

    print_bday_information(interval)


main()
