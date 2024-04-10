from datetime import date
import sys
import inflect

# set up for inflect
p = inflect.engine()


def main():
    try:
        year, month, day = input("Date of Birth: ").split('-')
        # .days used to get number of days from the difference between two dates.
        age_days = (date.today() - date(int(year), int(month), int(day))).days
        print(calculate_age_in_minutes(age_days))
    except:
        raise sys.exit("Invalid date")

def calculate_age_in_minutes(age_days):
    age_minutes = age_days * 24 * 60
    # method in inflect to change number to text
    return f"{p.number_to_words(age_minutes, andword="")} minutes".capitalize()

if __name__ == "__main__":
    main()
# check50 cs50/problems/2022/python/seasons
