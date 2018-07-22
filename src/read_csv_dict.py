import sys
import csv


def read_csv_dict(input):
    """
    :param input: a fully qualified csv file name to read data from
    :return: read and build a dictionary
    """

    listdicts = []
    with open(input, mode='r') as read:
        csvtext = csv.DictReader(read)
        keys = csvtext.fieldnames
        for row in csvtext:
            listdicts.append(row)

        for key in keys:
            print(key, listdicts[160][key])


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
        read_csv_dict(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
