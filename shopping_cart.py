


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

item_entry = input("Enter Numeric Item ID Here; When Complete, Enter DONE: ")
matching_products = [i for i in products if str(i["id"]) == str(item_entry)]
matching_product = matching_products[0]
print("SELECTED PRODUCT " + matching_product["name"] + " " + str(matching_product["price"]))

#
# INFO DISPLAY / OUTPUT
#

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

#print(create_list)



# item = (purchase_items)
# print(item)

# Please input a product identifier: 2
# Please input a product identifier: 3
# Please input a product identifier: 2
# Please input a product identifier: 1
# Please input a product identifier: DONE

# print("---------------------------------")
# print("WEGMANS")
# print("www.Wegmans.com")
# print("Don't forget to Download the Wegmans App")
# print("---------------------------------")
# #> CHECKOUT AT: 2020-02-07 03:54 PM
# print("---------------------------------")
# #> SELECTED PRODUCTS:
# #>  ... Chocolate Sandwich Cookies ($3.50)
# #>  ... All-Seasons Salt ($4.99)
# #>  ... Robust Golden Unsweetened Oolong Tea ($2.49)
# #>  ... All-Seasons Salt ($4.99)
# #>  ... Chocolate Sandwich Cookies ($3.50)
# print("---------------------------------")
# #> SUBTOTAL: $19.47
# #> TAX: $1.70
# #> TOTAL: $21.17
# print("---------------------------------")
# print("THANKS, SEE YOU AGAIN SOON!")
# print("---------------------------------")