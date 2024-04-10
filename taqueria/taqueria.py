menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
 place_order()

def place_order():
 order = []
 try:
    while True:
        # title makes every word start with uppercase
        item = input("Item (press Ctrl-D to finish): ").title()
        if item in menu:
            # append allows adding to a list
            order.append(item)
            total_cost = calculate_total(order)
            print(f"Total: ${total_cost:.2f}")
 except EOFError:
    pass
 except KeyError:
    pass

def calculate_total(order):
   total = 0
   for item in order:
      # get returns the value if the key is inside the dict. Second item would be a default of
      # None so made it a 0 as you can't add None to a number
      total += menu.get(item, 0)
   return total

main()

# check50 cs50/problems/2022/python/taqueria
