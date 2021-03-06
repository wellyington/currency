from google_currency import convert
import argparse
import json
currency_parser = argparse.ArgumentParser()
currency_parser.add_argument('-f', '-from', action='store', type=str, required=True, help='Base Currency Code - Example: EUR')
currency_parser.add_argument('-t', '-to', action='store', type=str, required=True, help='Target Currency Code - Example: USD')
currency_parser.add_argument('-a', '-amount', action='store', type=str, required=True, help='Amount to exchange - Example: 99.99')
args = currency_parser.parse_args()
cFrom = args.f
cTo = args.t
cAmount = float(args.a)
currency = convert(cFrom, cTo, cAmount)
currencyConvert = json.loads(currency)
print("Converted: " + str(cAmount) + " " + cFrom + " To: " + currencyConvert['amount'] + " " + cTo)