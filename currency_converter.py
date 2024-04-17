from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "fca_live_JRs0dDenyW5t68l1cngi16iCyBSmJumNhk3NQHFj"
printer = PrettyPrinter()

def get_Currency():
    endpoint = f"v1/latest?apikey=fca_live_JRs0dDenyW5t68l1cngi16iCyBSmJumNhk3NQHFj"
    url = BASE_URL + endpoint
    data = get(url).json()['data']

    data = list(data.items())
    data.sort()
    return data

def convert(currency1, currency2, amount):
    data = get_Currency()
    endpoint = f"v1/latest?apikey={API_KEY}&currencies={currency2}&base_currency={currency1}"
    url = BASE_URL + endpoint
    data = get(url).json()['data']

    if data is None:
        return
    try: 
        amount = float(amount)
    except:
        print("Invalid amount.\n")
        return

    first = data[currency2]
    total = amount* first
    print(f"The new total is now: {total:.2f}")


def main():
    print("Welcome to the currency converter!")
    print("Fetching available currencies...")
    currencies = get_Currency()
    printer.pprint(currencies)

    first_currency = input("Provide the first currency: ")
    second_currency = input("Converted to: ")
    price = input("For how much: ")

    convert(first_currency, second_currency, price)

if __name__ == "__main__":
    main()