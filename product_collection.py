products = ["TV", "Fridge", "Washing Machine", "Mobile Phone", "Car", "Bike"]
# print(products)
sample_product = ("Mobile Phone", 50000, "Electronic")

# Printing 2nd and last products from the list
# print(products[1])
# print(products[-1])

# Appending 2 new products in list and print the updated list
products.append("Bottle")
products.append("Pen")
# print(list(products))

# Converting sample_product into list
sample_product = list(sample_product)
sample_product[1] = 54000
sample_product = tuple(sample_product)
# print(sample_product)

