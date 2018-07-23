"""
This module takes a CSV file as input,
creates python friendly headers, does string
clean up and type conversion and then output.
"""

import sys
import csv
import src.msds510.utils_midterm as utils


def process_csv(input, output):
    """
    :param input: Input file name
    :param output: Output file name
    :return: File with python friendly column header
    and formatted data rows
    """
    with open(input, mode='r') as read:
        csvtext = csv.DictReader(read)

        keys = csvtext.fieldnames

        with open(output, mode='w') as write:
            processedtext = csv.DictWriter(write, fieldnames=keys)
            colheader = {}
            for key in keys:
                colheader[key] = utils.str_convert(key)

            processedtext.writerow(colheader)

            for row in csvtext:
                row = utils.transform_record(row)
                processedtext.writerow(row)


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
        process_csv(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    # execute only if run as a script
    main()
