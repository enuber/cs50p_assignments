import sys
import csv

def main():
    check_args()
    check_valid_file_type()
    clean_code()

def check_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguements")

def check_valid_file_type():
    if '.csv' not in sys.argv[1] and '.csv' not in sys.argv[2]:
        sys.exit("Not a CSV file")

def clean_code():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    try:
        with open(input_file, 'r') as in_file:
            reader = csv.DictReader(in_file)
            with open(output_file, 'w') as out_file:
                writer = csv.DictWriter(out_file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    last_name, first_name = row['name'].split(',')
                    writer.writerow({
                        # just checking that it doesn't matter which order these are in. Still outputs correctlycheck50 cs50/problems/2022/python/scourgify

                        "last": last_name.strip(),
                        "first": first_name.strip(),
                        "house": row["house"]
                    })

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/scourgify
