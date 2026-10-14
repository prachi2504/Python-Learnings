price_dict = {
    "TV": 24000, 
    "Fridge": 18000,
    "Washing Machine": 30000,
    "Mobile Phone": 58000,
    "Car": 98000,
    "Bike": 85000
}
# print(price_dict)
# Adding a product with price to the dict.
price_dict["Bottle"] = 2000
price_dict["Pen"] = 250
# print(price_dict)

# Updating price of existing product
price_dict["Car"] = 100000
# print(price_dict)

# Removing product by name
remove_product = "Mobile"
if remove_product in list(price_dict.keys()):
    price_dict.pop(remove_product)
# print(price_dict)

# Average of products prices
number = 0
for a in list(price_dict.values()):
    number += a
# print(number / len(price_dict))

# Product with Maximum Price
maximum_price = 0
max_price_product = ""
for pp, pk in price_dict.items():
    if pk > maximum_price:
        maximum_price = pk
        max_price_product = pp
# print(dict({max_price_product : maximum_price}))

# Product with Minimum Price
minimum_price = maximum_price
min_price_product = ""
for pp, pk in price_dict.items():
    if pk < minimum_price:
        minimum_price = pk
        min_price_product = pp
# print(dict({min_price_product : minimum_price}))