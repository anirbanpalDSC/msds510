import sys
import csv


"""Function to try get arguments that will not
crash program if argument out of bounds"""


def check_argument(index):
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]


"""Take a CSV file as input and extract any given row"""


def read_csv_dict(input):
    listdicts = []
    with open(input, mode='r') as read:
        csvtext = csv.DictReader(read)
        keys = csvtext.fieldnames
        for row in csvtext:
            listdicts.append(row)

        for key in keys:
            print(key, listdicts[160][key])


if __name__ == "__main__":
    input = check_argument(1)

    if input:  # argument is valid
        read_csv_dict(input)
