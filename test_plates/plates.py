def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return check_length(s) and check_first_two_characters(s) and nums_and_letters(s) and check_numbers(s)

def check_length(s):
    return 2 <= len(s) <= 6

def check_first_two_characters(s):
    return s[0].isalpha() and s[1].isalpha()

def nums_and_letters(s):
    return s.isalnum()

def check_numbers(s):
    for i in range(len(s)):
        if s[i].isdigit() and int(s[i]) != 0:
            correct_index = s.index(s[i])
            position = len(s) - correct_index
            for j in s[-position:]:
                if not j.isdigit():
                    return False
            return True
        elif s[i].isdigit() and int(s[i]) == 0:
            return False
    return True

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/tests/plates
