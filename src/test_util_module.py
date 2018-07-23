"""
This module has the test scripts to
test other modules in the project.
"""

from src.utils import get_date_joined, days_since_joined

records = [
    dict(year='1988', intro='Jun-88'),
    dict(year='1989', intro='May-89'),
    dict(year='2005', intro='5-May'),
    dict(year='2013', intro='13-Nov'),
    dict(year='2014', intro='14-Jan')
]

for record in records:

    print("Input Record -", record)

    dtJoin = get_date_joined((record['year']), (record['intro']))

    print("Date Joined -", dtJoin)

    dyJoined = days_since_joined((record['year']), (record['intro']))

    print("Days since Joined -", dyJoined, '\n')
