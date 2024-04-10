def main():
    amount_paid = get_coins()
    give_change(amount_paid)

def get_coins():
    coins = 0
    while True:
        amount = int(input("Insert Coin: "))
        if amount == 5 or amount == 10 or amount == 25:
            coins += amount
            if coins >= 50:
                return coins
            else:
                print(f'Amount Due: {50 - coins}')
        else:
            print(f'Amount Due: {50 - coins}')

def give_change(coins):
    print(f'Change Owed: {coins - 50}')

main()
# check50 cs50/problems/2022/python/coke
