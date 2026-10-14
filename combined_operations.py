import product_pricing, product_collection, Categories

product_list = product_collection.products
product_categories = Categories.categories

# catalog of product_name, price and category:
catalog = []
for i, product_name in enumerate(product_list):
    catalog.append(tuple([  
        product_name,
        product_pricing.price_dict.get(product_name),
        product_categories[i]
    ]))
print(f"Value of Catalog is :\n {catalog}")

# dictionary of catagory to product:
category_to_product = dict({})
for product in catalog:
    category_to_product.update({
        product[2] : product[0]
    })
print(f"Value of category_to_ptoduct is :\n {category_to_product}")

# catagory with maximum number of product
i = 0
category = ""
for ct in set(category_to_product.keys()):
    if i < len(category_to_product.get(ct)):
        i = len(category_to_product.get(ct))
        category = ct
print(f"Maximum number of product are for {category} category, number of products are {i}")