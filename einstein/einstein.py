def main():
    mass = int(input('Enter a mass : '))
    print('E:', findJoules(mass))

def findJoules(mass):
    speed_of_light = 300000000
    return mass * speed_of_light ** 2

main()

# check50 cs50/problems/2022/python/einstein
