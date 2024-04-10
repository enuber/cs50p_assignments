def main():
    answer = input('What is the answer to the Great Question of Life, the Universe and Everything? ').strip().lower()
    match answer:
        case '42' | 'forty-two' | 'forty two':
            print('Yes')
        case _:
            print('No')

main()

# check50 cs50/problems/2022/python/deep
