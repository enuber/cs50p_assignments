import requests
import sys

def get_bitcoin_price(amount_entered):
    try:
        amount_entered = float(amount_entered)
    except ValueError:
        print('Command-line argument is not a number')

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        current_price = data['bpi']['USD']['rate_float']
        return current_price * float(amount_entered)
    except:
        sys.exit('can\'t retrieve current price')
yes
def main():
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')
    bitcoin_amount_entered = sys.argv[1]
    actual_cost = get_bitcoin_price(bitcoin_amount_entered)
    print(f"${actual_cost:,.4f}")

if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/bitcoin
