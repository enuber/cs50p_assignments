def main():
    word = input('camelCase: ')
    snake_case = make_snake_case(word)
    print(snake_case)

def make_snake_case(word):
    snake_case = ''
    for character in word:
        if character.isupper():
            snake_case += '_' + character.lower()
        else:
            snake_case += character
    # in case the word entered started with a capital letter, need to remove the underscore
    return snake_case.lstrip('_')


main()

# check50 cs50/problems/2022/python/camel
