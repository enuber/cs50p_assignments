def main():
    greeting = input('Enter a greeting. ').strip().lower()
    amount_owed = value(greeting)
    print(f"${amount_owed}")

def value(greeting):
    if greeting.startswith('hello'):
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/tests/bank
