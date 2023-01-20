#  ReceiptGenius

A simple system designed to speed up the process of producing receipts for customers.

---

## Technologies, Libraries & Installation

This project leverages python 3.7. Docs below:

* [python](https://docs.python.org/3/)
* [argparse](https://docs.python.org/3/library/argparse.html)

---

## Main Walkthrough

1. First, a Receipt class is created to store information about the receipt such as the customer's name, purchase items, and total cost.

```
class Receipt:
    def __init__(self, customer_name, items, total_cost):
        self.customer_name = customer_name
        self.items = items
        self.total_cost = total_cost
```

2. Next, we create a function called generate_receipt that takes in a Receipt object and generates a receipt in the form of a string that can be printed or saved as a file.
```
def generate_receipt(receipt):
    receipt_str = "Receipt for {}\n".format(receipt.customer_name)
    for item in receipt.items:
        receipt_str += "- {}: ${}\n".format(item[0], item[1])
    receipt_str += "Total: ${}".format(receipt.total_cost)
    return receipt_str
```

3. Finally, we create a function called print_receipt that takes in a Receipt object and uses the generate_receipt function to print the receipt
```
def print_receipt(receipt):
    receipt_str = generate_receipt(receipt)
    print(receipt_str)
```

4. To use the system, a new Receipt object is created, fill in the customer's name, purchase items and total cost, and then call the print_receipt function to print the receipt.

```new_receipt = Receipt("John Smith",[("item1",10.5),("item2",5)],15.5)
print_receipt(new_receipt)
```

This is just a simple example, and in a real-world scenario, you may want to consider additional features such as the ability to save receipts as files, or to print receipts on a physical printer.

---

## CLI Tool Usage

Run the script from the command line and pass in the necessary arguments

```
python receipt_tool.py --name "John Smith" --items "item1:10.5,item2:5" --total 15.5
```

## Contributors

*  **Quintin Bland** <span>&nbsp;&nbsp;</span> |
<span>&nbsp;&nbsp;</span> *email:* quintinbland2@gmail.com <span>&nbsp;&nbsp;</span>|
<span>&nbsp;&nbsp;</span> <a href="https://www.linkedin.com/in/quintin-bland-a2b94310b/"><img src="https://img.shields.io/badge/-Quintin_Bland-0077B5?style=flat-square&logo=Linkedin&logoColor=white"/></a> 

---

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
