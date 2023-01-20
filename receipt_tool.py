import argparse
from main import Receipt, print_receipt

# Instantiate ArgumentParser
parser = argparse.ArgumentParser()


# Adding arguments
parser.add_argument('--name', require=True, type=str, help='Customer name')
parser.add_argument('--items purchased', require=True, type=str, help='items purchased')
parser.add_argument('--total', require=True, type=str, help='Total cost')

# parse command line args and call the print_receipt function, passing in receipt
args = parser.parse_args()
items = [tuple(item.split(':')) for item in args.items.split(',')]
new_receipt = Receipt(args.name, items, args.total)
print_receipt(new_receipt)


