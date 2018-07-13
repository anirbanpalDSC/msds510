import sys
import csv


def check_argument(index):  # function to try get arguments that will not crash program if argument out of bounds
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]


"""Take a CSV file as input and extract any given row"""


def read_csv(input):
    rows = []
    with open(input, mode='r') as read:
        csvtext = csv.reader(read)
        for row in csvtext:
            rows.append(row)

        print(rows[161])


if __name__ == "__main__":
    input = check_argument(1)

    if input:  # argument is valid
        read_csv(input)
