def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    amount = gauge(percentage)
    print(amount)

def convert(fraction):
    try:
        x, y = fraction.split('/')
        percentage = int(round((int(x)/int(y))*100))
        if 0 <= percentage <= 100:
            return percentage
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/tests/fuel
