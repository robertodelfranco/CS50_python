import sys
import requests

def main():
    if len(sys.argv) == 2:
        try:
            buy = float(sys.argv[1])
            get_value(buy)
        except ValueError:
            sys.exit("Command-line argment is not a number")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    else:
        sys.exit("Missing command-line argument")


def get_value(buy):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    text = response.json()

    rate = text["bpi"]["USD"]["rate"].replace(",", "")

    print(f"${buy * float(rate):,.4f}")

main()
