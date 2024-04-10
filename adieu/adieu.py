import sys
import inflect

def bid_adieu(names):
    p = inflect.engine()
    # per documentation can use p.join on a list to join comma separated  with last having an and
    print(f"\nAdieu, adieu, to {p.join(names)}")

def main():
    names = []
    while True:
        try:
            name = input('Name: ')
            names.append(name)
        except EOFError:
            # breaking rather than printing here to verify names list. could be done here though as well.
            break
    # just in case no names are given
    if len(names) < 1:
        sys.exit()
    bid_adieu(names)


main()

# check50 cs50/problems/2022/python/adieu
