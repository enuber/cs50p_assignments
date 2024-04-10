import sys

def main():
    check_args()
    check_valid_file_type()
    file = open_file()
    count_lines(file)

def check_args():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguements")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguements")

def check_valid_file_type():
    if '.py' not in sys.argv[1]:
        sys.exit("Not a Python file")

def open_file():
    try:
        return(open(sys.argv[1], "r"))
    except FileNotFoundError:
        sys.exit("File does not exist")

def count_lines(file):
    total_lines = 0
    lines = file.readlines()
    for line in lines:
        if len(line.lstrip()) != 0 and not line.lstrip().startswith("#"):
            total_lines += 1
    print(total_lines)


if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/lines
