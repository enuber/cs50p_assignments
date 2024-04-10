def main():
    word = input("Input: ")
    word_without_vowels = shorten(word)
    print(word_without_vowels)

def shorten(word):
    new_word = ''
    vowels = 'aeiouAEIOU'
    for letter in word:
        if letter not in vowels:
            new_word += letter
    return new_word

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/tests/twttr
