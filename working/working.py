import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    # notes: \d for digit and (AM|PM) the pipe "|" is "or"
    # {m} - repetiions, {m, n} - m-n repetitions
    # may need two patterns as if you do :? it would run the digits together if there isn't a colon.
    pattern = r'^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$'

    match = re.match(pattern, s)

    if match:
        starting_hour, starting_minutes, starting_meridiem, ending_hour, ending_minutes, ending_meridiem = match.groups()
    else:
        raise ValueError('Invalid input format')

    # make integers
    starting_hour = int(starting_hour)
    if starting_minutes != None:
        starting_minutes = int(starting_minutes)
    ending_hour = int(ending_hour)
    if ending_minutes != None:
        ending_minutes = int(ending_minutes)

    # validate hours and minutes
    if not(0 <= starting_hour <= 12 and 0 <= ending_hour <= 12):
        raise ValueError('Invalid hours entered')
    if starting_minutes != None:
        if not(0 <= starting_minutes < 60):
            raise ValueError('Invalid minutes entered')
    else:
        starting_minutes = 0
    if ending_minutes != None:
        if not(0 <= ending_minutes < 60):
            raise ValueError('Invalid minutes entered')
    else:
        ending_minutes = 0

    # change to 24 hour format
    if starting_meridiem == "PM" and starting_hour != 12:
        starting_hour += 12
    if starting_meridiem == "AM" and starting_hour == 12:
        starting_hour = 0

    if ending_meridiem == "PM" and ending_hour != 12:
        ending_hour += 12
    if ending_meridiem == "AM" and ending_hour == 12:
        ending_hour = 0

    return f"{starting_hour:02d}:{starting_minutes:02d} to {ending_hour:02d}:{ending_minutes:02d}"

if __name__ == "__main__":
    main()

    # check50 cs50/problems/2022/python/working

