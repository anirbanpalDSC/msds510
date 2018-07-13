import sys


def check_argument(index):  # function to try get arguments that will not crash program if argument out of bounds
    try:
        sys.argv[index]
    except IndexError:
        return ''
    else:
        return sys.argv[index]


"""Take binary file as input and convert to UTF-8"""


def convert_to_utf8(input, output):
    file = open(input, encoding='ISO-8859-1', errors='ignore')
    data = file.read()
    with open(output, mode='w', encoding='UTF-8') as file:
        file.write(data)


if __name__ == "__main__":
    input = check_argument(1)
    output = check_argument(2)
    if input and output:  # both arguments are valid
        convert_to_utf8(input, output)
