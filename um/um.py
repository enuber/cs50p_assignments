import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # note that \b alone represents a word boundry. By surrounding "um" with \b it is ensured that we only grab the cases where um is a stand
    # alone word.
    return len(re.findall(r'\bum\b', s, re.IGNORECASE))

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/um
