"""
Helper module for mid-term project.
"""

import datetime as dt
import csv

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

    # Extract the three characters after first
    # alphabet and convert to lower to have 'mon'
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
    :param strYr: Year
    :param strIP: Month name
    :return: Date since joined as of today
    """
    try:
        dtFrom = get_date_joined(strYr, strIP)
        dtToday = dt.date.today()
        dtDays = (dtToday - dtFrom).days
        return dtDays
    except Exception:
        raise ValueError("Not a date")


def to_int(anyVal):
    intVal = int(anyVal)
    return intVal


def to_bool(anyVal):
    if anyVal.lower() in ("yes", "true", "t", "1"):
        return True
    elif anyVal.strip() == "":
        return ""
    else:
        return False


def clean_notes(anyStr):
    """
    :param anyStr: string
    :return: string with newline replaced
    """
    outStr = anyStr.rstrip("\n")
    return outStr


def transform_record(dic):
    """
    :param dic: dictionary
    :return: data type converted dictionary
    """

    curryr = dt.datetime.today().year
    for k, v in dic.items():
        if k in ("year", "appearances"):
            dic[k] = to_int(v)
        if k.startswith("death") | k.startswith("return") | k == "current":
            dic[k] = to_bool(v)
        if k == "notes":
            dic[k] = clean_notes(v)
        if k == "years_since_joining":
            dic[k] = curryr - dic["year"]
    return dic


def str_convert(input):
    """
    :param input: string
    :return: formatted string
    """
    if "re" not in dir():
        import re

    output = re.sub(" |//|\/", "_", input).lower().rstrip("?|\n")
    return output


def read_csv_dict(input):
    """
    :param input: a fully qualified csv file name
    :return: dictionary
    """

    listdicts = []
    with open(input, mode='r') as read:
        csvtext = csv.DictReader(read)
        keys = csvtext.fieldnames
        for row in csvtext:
            row = transform_record(row)
            listdicts.append(row)

        for key in keys:
            print(key, listdicts[160][key])
