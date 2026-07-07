import requests
import sys


try:
   amount_wanted = float(sys.argv[1])

except ValueError:
    sys.exit("Command-line argument is not a number")

except IndexError:
    sys.exit("Missing command-line argument")




try:
    web = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=b4a7a58c789802e46c45b509365c83362d9bbf83c6fc6dcd7d208d10ebcea722")
except requests.RequestException:
    sys.exit("Couldn't make the request")


response = web.json()
price = float((response["data"]["priceUsd"]))

cost = price * amount_wanted
print(f"${cost:,.4f}")





