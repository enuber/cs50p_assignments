def main():
    fraction = get_fraction("Fraction: ")
    amount = fraction_to_percent(fraction)
    print(amount)

def get_fraction(prompt):
    while True:
        try:
            num = input(prompt)
            x, y = num.split('/')
            percentage = (int(x)/int(y)) * 100
            if 0 <= percentage <= 100:
                return percentage
        except (ValueError, ZeroDivisionError):
            pass

def fraction_to_percent(num):
    if num <= 1:
        return 'E'
    elif num >= 99:
        return 'F'
    else:
        return (f"{round(num)}%")

main()

# check50 cs50/problems/2022/python/fuel
