# from datetime import datetime, date, time, timezone

# now = datetime.now()

# #print(now)

# dt = now.strftime("%A, %B %d, %Y %I:%M %p")

# print(dt)




#
# INFO CAPTURE/INPUT
#

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


#
# INFO CAPTURE/INPUT
#

subtotal = 0
groceries = []

while True:
    item_entry = input("Enter Numeric Item ID Here; When Complete, Enter DONE: ")
    if item_entry == "DONE":
        break
    elif [p for p in products if str(p["id"]) == item_entry]:
        groceries.append(item_entry)
    else:
        print("Unrecognized Item. Please Re-Enter.")

# Date and Time
#now = datetime.now()
#dt = now.strftime("%A, %B %d, %Y %I:%M %p")


#
# INFO DISPLAY / OUTPUT
#

#print(groceries)

def to_usd(my_price):
    return f"${my_price:,.2f}"

# print("---------------------------------")
# print("WEGMANS")
# print("21 Flushing Ave")
# print("Brooklyn, NY 11205")
# print("(347) 694-8510")
# print("www.Wegmans.com")
# print("---------------------------------")
# print(dt)
# print("---------------------------------")

# for item_entry in groceries:
#     matching_products = [i for i in products if str(i["id"]) == str(item_entry)]
#     matching_product = matching_products[0]
#     subtotal = subtotal + matching_product[("price")]
#     print("............. " + matching_product["name"] + " " + to_usd(str(matching_product[("price"))))

#Sent to ANUSHA
for item_entry in groceries:
     matching_products = [i for i in products if str(i["id"]) == str(item_entry)]
     matching_product = matching_products[0]
     subtotal = subtotal + matching_product["price"]
     print("............. " + matching_product["name"] + " " + str(to_usd(matching_product["price"])))

tax = subtotal * .0875

amount_owed = tax + subtotal

print("SUBTOTAL: " + str(to_usd((subtotal))))
print("TAX: " + str(to_usd(tax)))
print("TOTAL BILL: " + str(to_usd(amount_owed)))




#def purchase_items(i):
       #if i == products["id"]:
    #    return item_entry
    #elif i == "DONE":
    #    return ("print receipt")
    # else:
    #     return ("Invalid entry. Please input product number between 1 and 20 or DONE")
    

# def to_usd(my_price):
#     """
#     Converts a numeric value to usd-formatted string, for printing and display purposes.

#     Param: my_price (int or float) like 4000.444444

#     Example: to_usd(4000.444444)

#     Returns: $4,000.44
#     """
#     return f"${my_price:,.2f}" #> $12,000.71



#print(products)

#(shopping-env)  --->> python shopping_cart.py

#item_entry = int(input("Enter Numeric Item ID Here, when complete enter DONE: "))

# def create_list(i):
#     item_entry = float(input("Enter Numeric Item ID Here; When Complete, Enter DONE: "))
#     groceries = []
#     while "DONE":
#         if i <= 20:
#             return(item_entry)
#         elif i >= 1:
#             return(item_entry)
#         else:
#             return ("Invalid entry." + (item_entry))
#         shopping.append(item_entry)
#     return groceries

=