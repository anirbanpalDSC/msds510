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

# Converts a month name to number
def get_month(strIP):

    # Remove leading or trailing spaces from a string in Python
    strIP = strIP.strip()

    # Get the first alpha character in the input string
    for index in range(len(strIP)):
        if strIP[index].isalpha():
            break

    # Extract the three characters after first alphabet and convert to lower to have 'mon'
    strMon = strIP[index:(index+3)].lower()

    # Convert month abbr/name to month number
    try:
        return month_dict[strMon]
    except Exception:
        raise ValueError("Not a month")

# Provides year, month and first day of month, given the year and month name
def get_date_joined(strYr,strIP):
    try:
        intYr = int(strYr)
        strOP = dt.date(intYr, get_month(strIP), 1)
        return strOP
    except Exception:
        raise ValueError("Not a date")

# Returns the integer number of days since the input date from today's date
def days_since_joined(strYr,strIP):
    try:
        dtFrom = get_date_joined(strYr,strIP)
        dtToday = dt.date.today()
        dtDays = (dtToday - dtFrom).days
        return dtDays
    except Exception:
        raise ValueError("Not a date")








