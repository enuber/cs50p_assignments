

def main():
    grocery_list = make_list()
    print_list(grocery_list)

def make_list():
 grocery_list = {}
 while True:
    try:
        item = input().strip().lower()
        if item in grocery_list:
            grocery_list[item] = grocery_list.get(item, 0) + 1
        else:
           grocery_list[item] = 1
    except EOFError:
        break
    except KeyError:
        pass
 return grocery_list

def print_list(grocery_list):
    print()
    for item, count in sorted(grocery_list.items()):
        print(f"{count} {item.upper()}")

main()

# check50 cs50/problems/2022/python/grocery
