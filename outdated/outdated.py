months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    get_date()

def get_date():
    while True:
        try:
            date = input("Date: ").strip().title()
            if '/' in date:
                month, day, year = date.split('/')
                valid = validate_date(month, day, year)
                if valid:
                    setup_date(month, day, year)
                    break
            else:
                month, day, year = date.split(' ')
                day = day[:-1]
                month = str(valid_month_in_list(month))
                valid = validate_date(month, day, year)
                if valid:
                    setup_date(month, day, year)
                    break
        except ValueError:
            pass

def valid_month_in_list(month):
    try:
        return months.index(month) + 1
    except ValueError:
        return None

def validate_date(month, day, year):
    if month.isdigit() and day.isdigit() and year.isdigit():
        if (1 <= int(month) <= 12) and (1 <= int(day) <= 31) and int(year) >=1:
            return True
        else:
            return False
    return False

def setup_date(month, day, year):
    print(f"{year}-{int(month):02}-{int(day):02}")


main()

# check50 cs50/problems/2022/python/outdated
