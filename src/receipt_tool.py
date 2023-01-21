import argparse
from main import Receipt, print_receipt, save_receipt, print_receipt_physical

# Instantiate ArgumentParser
parser = argparse.ArgumentParser()


# Adding arguments
parser.add_argument('--name', require=True, type=str, help='Customer name')
parser.add_argument('--items purchased', require=True, type=str, help='items purchased')
parser.add_argument('--total', require=True, type=str, help='Total cost')
parser.add_argument('--save', type=str, help='save receipt in file')
parser.add_argument('--print', action='store_true', help='print receipt')

# parse command line args and call the print_receipt function, passing in receipt
args = parser.parse_args()
items = [tuple(item.split(':')) for item in args.items.split(',')]
new_receipt = Receipt(args.name, items, args.total)
print_receipt(new_receipt)

# check if the user wants to save or print the receipt
# call the appropriate function based on their choice
if args.save:
    save_receipt(new_receipt, args.save)
if args.print:
    print_receipt_physical(new_receipt)






