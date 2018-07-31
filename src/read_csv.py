"""
This module takes input CSV file as the
only argument and prints the 162nd row.
"""

import sys
import csv


def read_csv(input):
    """
    :param input: a fully qualified file name (csv) to read data from
    :return: print the rows
    """
    rows = []
    with open(input, mode='r') as read:
        csvtext = csv.reader(read)
        for row in csvtext:
            rows.append(row)

        print(rows[161])


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
        read_csv(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
