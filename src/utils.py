"""
This module is part of assignment 6.1 and NOT the
mid term project. But it is kept in the same
directory structure as per the instruction. It has the
helper functions for the assignment.
"""

import datetime as dt

# Define the month dictionary
month_dict = dict(jan=1,
                  feb=2,
                  mar=3,
                  apr=4,
                  may=5,
                  jun=6,
                  jul=7,
                  aug=8,
                  sep=9,
                  oct=10,
                  nov=11,
                  dec=12)


def get_month(strIP):
    """
    :param strIP: Month name
    :return: Month number
    """

    # Remove leading or trailing spaces from a string in Python
    strIP = strIP.strip()

    # Get the first alpha character in the input string
    for index in range(len(strIP)):
        if strIP[index].isalpha():
            break

    # Extract the three characters after first alphabet
    # and convert to lower to have 'mon'
    strMon = strIP[index:(index+3)].lower()

    # Convert month abbr/name to month number
    try:
        return month_dict[strMon]
    except Exception:
        raise ValueError("Not a month")


def get_date_joined(strYr, strIP):
    """
    :param strYr: Year
    :param strIP: Month name
    :return: Joining date
    """
    try:
        intYr = int(strYr)
        strOP = dt.date(intYr, get_month(strIP), 1)
        return strOP
    except Exception:
        raise ValueError("Not a date")


def days_since_joined(strYr, strIP):
    """
    :param strYr: Int year of joining
    :param strIP: Month name
    :return: days since joined, as of today
    """
    try:
        dtFrom = get_date_joined(strYr, strIP)
        dtToday = dt.date.today()
        dtDays = (dtToday - dtFrom).days
        return dtDays
    except Exception:
        raise ValueError("Not a date")
