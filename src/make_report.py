"""
This module reads an input csv file, sorts the
content, keeps top 10 appearances and sends the
sorted and filtered records and an outfile destination
to to_markdown to print
"""

import sys
import csv
from src.msds510.avenger import Avenger as av


def make_report(input, output):
    """
    :param input: a fully qualified file name (csv) to read data from
    :param output: a fully qualified destination file name (md)
    :return: executes the to_markdown function with sorted records and writes
    the results to and outfile.
    """

    file = []
    with open(input, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        file = list(reader)

    sortedRecords = sorted(file,
                           key=lambda k: int(k['appearances']),
                           reverse=True)[:10]

    avenger = av()
    avenger.to_markdown(sortedRecords, output)


def main():
    """
    interprets command line request
    :return: Creates the output csv file in the specified location
    """

    if len(sys.argv) != 3:
        print("this report generator takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        make_report(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    # execute only if run as a script
    main()
