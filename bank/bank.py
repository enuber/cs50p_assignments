def main():
    greeting = input('Enter a greeting. ').strip().lower()
    checkGreeting(greeting)

def checkGreeting(greeting):
    if greeting.startswith('hello'):
        print('$0')
    elif greeting.startswith('h'):
        print('$20')
    else:
        print('$100')

main()

# check50 cs50/problems/2022/python/bank
