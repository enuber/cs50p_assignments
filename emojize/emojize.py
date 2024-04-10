import emoji

def make_emoji_phrase(text):
    return emoji.emojize(text, language='alias')


def main():
    user_input = input("Input: ")
    emoji_phrase = make_emoji_phrase(user_input)
    print("Output:", emoji_phrase)

main()

# check50 cs50/problems/2022/python/emojize
