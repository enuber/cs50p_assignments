import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        tries = 0

        while tries < 3:
            guess = input(f"{x} + {y} = ")
            try:
                guess = int(guess)
                if guess == answer:
                    score += 1
                    break
                else:
                    tries += 1
                    print("EEE")
            except ValueError:
                print("EEE")

        if tries == 3:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/professor
