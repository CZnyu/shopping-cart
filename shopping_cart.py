from datetime import datetime, date, time, timezone
import csv
import os

csv_filepath = os.path.join(os.path.dirname(__file__), "data", "product_list.csv")

with open(csv_filepath, "r") as csv_file:
    products = []
    reader = csv.DictReader(csv_file)
    for row in reader:
        products.append(row)

#
# INFO CAPTURE/INPUT
#

subtotal = 0
groceries = []

while True:
    item_entry = input("Enter Numeric Item ID Here; When Complete, Enter DONE: ")
    if item_entry == "DONE":
        break
    elif item_entry == "done":
        break
    elif item_entry == "Done":
        break
    elif [p for p in products if str(p["id"]) == item_entry]:
        groceries.append(item_entry)
    else:
        print("Unrecognized Item. Please Re-Enter.")

# Date and Time
now = datetime.now()
dt = now.strftime("%A, %B %d, %Y %I:%M %p")

#
# INFO DISPLAY / OUTPUT
#

#print(groceries)

def to_usd(my_price):
    return f"${my_price:,.2f}"

print("---------------------------------")
print("WEGMANS")
print("21 Flushing Ave")
print("Brooklyn, NY 11205")
print("(347) 694-8510")
print("www.Wegmans.com")
print("---------------------------------")
print(dt)
print("---------------------------------")

for item_entry in groceries:
     matching_products = [i for i in products if str(i["id"]) == str(item_entry)]
     matching_product = matching_products[0]
     subtotal = subtotal + float(matching_product["price"])
     print(" + " + matching_product["name"] + " " + str(to_usd(float(matching_product["price"]))))

tax = subtotal * .0875

amount_owed = tax + subtotal

print("---------------------------------")
print("SUBTOTAL: " + str(to_usd((subtotal))))
print("TAX: " + str(to_usd(tax)))
print("TOTAL BILL: " + str(to_usd(amount_owed)))
print("TOTAL ITEMS PURCHASED: " + str(len(groceries)))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("Don't forget to Download the Wegmans App")
print("---------------------------------")

# A grocery store name of your choice - YES
# A grocery store phone number and/or website URL and/or address of choice - YES
# The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM) - YES
# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.) - YES
# The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices - YES
# The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax) - YES
# The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items - YES
# A friendly message thanking the customer and/or encouraging the customer to shop again - Yes


