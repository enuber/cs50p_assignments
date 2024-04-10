import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    try:
        if re.search(pattern, ip):
            return True
        else:
            return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/numb3rs
