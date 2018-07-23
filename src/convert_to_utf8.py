"""
This module takes an input file and
converts it to UTF-8 format output.
"""

import sys


def convert_to_utf8(input, output):
    """
    :param input: input binary file name
    :param output: output file name
    :return: UTF-8 Output file
    """

    file = open(input, encoding='ISO-8859-1', errors='ignore')
    data = file.read()
    with open(output, mode='w', encoding='UTF-8') as file:
        file.write(data)


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
        convert_to_utf8(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
