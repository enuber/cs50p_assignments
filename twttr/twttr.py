def main():
    word_without_vowels = remove_vowels()
    print(word_without_vowels)

def remove_vowels():
    word = input("Input: ")
    new_word = ''
    vowels = 'aeiouAEIOU'
    for letter in word:
        if letter not in vowels:
            new_word += letter
    return new_word

main()

# check50 cs50/problems/2022/python/twttr
