# receipt class to store receipt information
class Receipt:
    def __init__(self, customer_name, items, total_cost):
        self.customer_name = customer_name
        self.items = items
        self.total_cost = total_cost

# function to generate a string value for the receipt
def generate_receipt(receipt):
    receipt_str = "Receipt for {}\n".format(receipt.customer_name)
    for item in receipt.items:
        receipt_str += "- {}: ${}\n".format(item[0], item[1])
    receipt_str += "Total: ${}".format(receipt.total_cost)
    return receipt_str

# Function that takes in receipt and uses generate_receipt to print the receipt
def print_receipt(receipt):
    receipt_str = generate_receipt(receipt)
    print(receipt_str)

# To use the system, we will create a new_receipt object, fill in the customer's name, purchase items and total cost. 
# Then call the print_receipt function to print the receipt
new_receipt = Receipt("John Smith",[("item1",10.5),("item2",5)],15.5)
print_receipt(new_receipt)
