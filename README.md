# currency
Simple parsed Currency Exchange that I use on the terminal to avoid opening Google for exchanges rate all the time.

This Script uses the library 'Google Currency', 'argparse' and 'json'. To make sure you have them installed please use.

pip install google_currency // To install Google Currency lib
pip install argparse // To installl or update argparse module
pip install json // To install or update json module

USAGE: 

  -f F, -from F    Base Currency Code - Example: EUR
  -t T, -to T      Target Currency Code - Example: USD
  -a A, -amount A  Amount to exchange - Example: 99.99
  
EXAMPLE:

>> python currency.py -from EUR -to GBP -amount 49.99

  OR

>> python currency.py -f EUR -t GBP -a 49.99
