def main():
    input_str = input('Please enter a string: ')
    print(convert(input_str))

def convert(string):
    smile_face = "🙂"
    frown_face = "🙁"
    return string.replace(':)', smile_face).replace(':(', frown_face)

main()

# check50 cs50/problems/2022/python/faces
