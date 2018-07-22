import sys
import csv

import src.msds510.utils_midterm as utils


def process_csv(ip, op):
    with open(ip, mode='r') as read:
        csvtext = csv.DictReader(read)

        keys = csvtext.fieldnames

        with open(op, mode='w') as write:
            processedtext = csv.DictWriter(write, fieldnames=keys)
            colheader = {}
            for key in keys:
                colheader[key] = utils.str_convert(key)

            processedtext.writerow(colheader)

            for row in csvtext:
                row = utils.transform_record(row)
                processedtext.writerow(row)


def main():
    """interprets command line request
    Args:
        argv: an array with fully qualified input and output file names (csv)

    Returns:
        Creates the output csv file in the specified location.
    """
    if len(sys.argv) != 3:
        print("this report generator takes two parameters, "
              "an input file and an output file")
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        process_csv(sys.argv[1], sys.argv[2])


"""Take a CSV file as input and extract any given row"""

if __name__ == "__main__":
    # execute only if run as a script
    main()
