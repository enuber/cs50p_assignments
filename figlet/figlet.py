import sys
from pyfiglet import Figlet

figlet = Figlet()

def print_text(text, font):
    if font and font != None:
        figlet.setFont(font=font)
        print(figlet.renderText(text))
    else:
        print(figlet.renderText(text))


def main():
    font = None
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font = sys.argv[2]
        font_list = figlet.getFonts()
        if font in font_list:
            valid_font = True
        else:
            valid_font = False
            sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')


    if valid_font:
        text = input('input: ')
        print_text(text, font)

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/figlet
