import sys
import csv

from src.msds510.avenger import Avenger as av


def make_report(input, output):
    """reads an input csv file, sorts the content, keeps top 10 appearances
       and sends the sorted and filtered records and an outfile destination
       to to_markdown to print
    Args:
        infile: a fully qualified file name (csv) to read data from
        outfile: a fully qualified destination file name (md)
    Result:
        executes the to_markdown function with sorted records and an writes
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
    """interprets command line request
    Args:
        argv: an array with input and output file names (and path)

    Returns:
        no return. Execute make_report with collected file names.
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
