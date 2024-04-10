def main():
    time = input("What time is it (24hr time format): ")
    number = convert(time)
    meal = mealtime(number)
    if meal != None:
        print(meal)

def convert(time):
    hour, minutes = time.split(':')
    return int(hour) + int(minutes)/60

def mealtime(time):
    if 7.0 <= time <= 8.0:
        return 'breakfast time'
    elif 12.0 <= time <= 13.0:
        return 'lunch time'
    elif 18.0 <= time <= 19.0:
        return 'dinner time'
    else:
        return

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/meal
