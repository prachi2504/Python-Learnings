categories = ["Electronic", "Electronic", "Electronic", "Electronic", "Vehicle", "Vehicle", "Plastic", "Plastic"]
# print(categories)
categories_set = set(categories)
# print(categories_set)

# Adding a new category 
categories_set.add("Electrical")
categories_set.add("Electronic")
# print(categories_set)

# Check if category exist in set or not
# if "Electronic" in categories_set:
#     print(True)
# else:
#     print(False)

# Since we get unique items in set, let's find count of items from set.
unique_items = len(categories_set)
# print(f"Number of Unique items in categories list are : {unique_items}")