import requests
import sys


def main():
    # Check for correct amount of command line arguments
    if len(sys.argv) == 2:
        # Validate input is a number
        try:
            n = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        else:
            # Gets the price and fomats to print
            price = get_price(n)
            print(f"${price:,.4f}")

    # Usage error feedback
    elif len(sys.argv) == 1:
        sys.exit("Missing Command-line argument")
    else:
        sys.exit("Too many Command-line arguments")


def get_price(number):
    try:
        # Makes request to url and stores response in variable
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Request Error")
    else:
        # Format the response to json
        response = response.json()
        # return the value from the key, multiply it, and round it to 4 decimals
        return round(float(response["bpi"]["USD"]["rate_float"]) * number, 4)


if __name__ == "__main__":
    main()
