import sys
import csv
import re


"""Function to try get arguments that will not
crash program if argument out of bounds"""


def check_argument(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]


"""Take a string, convert to lower case,
replace space and slash with underscore
and strip trailing question marks and newlines """


def str_convert(str_input):
    str_ouptut = re.sub(" |//|\/", "_", str_input).lower().rstrip("?|\n")

    return str_ouptut


"""Take a CSV file as input and extract any given row"""


def write_csv(input, output):
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


if __name__ == "__main__":
    input = check_argument(1)
    output = check_argument(2)

    if input and output:  # both arguments are valid
        write_csv(input, output)
