import sys
import csv
from tabulate import tabulate

def main():
    check_args()
    check_valid_file_type()
    file = open_file()
    create_table(file)

def check_args():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguements")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguements")

def check_valid_file_type():
    if '.csv' not in sys.argv[1]:
        sys.exit("Not a CSV file")

def open_file():
    try:
        return(open(sys.argv[1], "r"))
    except FileNotFoundError:
        sys.exit("File does not exist")

def create_table(file):
    reader = csv.reader(file)
    # since reader is a list of strings, this converts it into a list of lists. So each inner list is a row
    # from the csv file and, each element in the inner list is a field within the row.

    data = list(reader)

    # tablefmt = 'grid' found in documentation, creates grid expected
    # header = also in doc setting this will mean headers are in first row

    print(tabulate(data, headers='firstrow', tablefmt='grid'))


if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/pizza
