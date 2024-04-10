import random
import sys

def get_level():
      while True:
        try:
            level = int(input("level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass

def main():
    level = get_level()
    target_number = random.randint(1, level)
    while True:
        try:
            guess = get_guess()

            if guess < target_number:
                print("Too small!")
            elif guess > target_number:
                print("Too large!")
            else:
                sys.exit("Just right!")
        except Exception:
            pass

main()

# check50 cs50/problems/2022/python/game
