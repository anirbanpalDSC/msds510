import sys
import csv
import re


def str_convert(str_input):
    """
    :param str_input: String
    :return: String, converted to lower case, replaced space and slash
    with underscore and strip trailing question marks and newlines
    """

    str_ouptut = re.sub(" |//|\/", "_", str_input).lower().rstrip("?|\n")

    return str_ouptut


"""Take a CSV file as input and extract any given row"""


def write_csv(input, output):
    """
    :param input: a fully qualified csv file name
    :param output: procesed csv file
    :return:
    """
    with open(input, mode='r') as read:
        csvtext = csv.DictReader(read)

        keys = csvtext.fieldnames

        with open(output, mode='w') as write:
            processedtext = csv.DictWriter(write, fieldnames=keys)
            colheader = {}
            for key in keys:
                colheader[key] = str_convert(key)

            processedtext.writerow(colheader)

            for row in csvtext:
                processedtext.writerow(row)


def main():
    """
    interprets command line request
    :return: Creates the output csv file in the specified location
    """

    if len(sys.argv) != 3:
        print('this report generator takes two parameters, '
              'an input file and an output file')
    else:
        print("input file: " + sys.argv[1])
        print("output file: " + sys.argv[2])
        write_csv(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
