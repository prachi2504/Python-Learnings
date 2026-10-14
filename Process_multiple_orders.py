order_amounts = [1200, 2500, 800, 900, 3000]

def calculate_discount(order_amount):
    if order_amount < 0:
        print("Invalid input. Order amount cannot be negative.")
    elif order_amount >= 2000:
        discount = order_amount * 0.15
        final_amount = order_amount - discount
    elif 1500 <= order_amount < 2000:
        discount = order_amount * 0.10
        final_amount = order_amount - discount
    elif 1000 <= order_amount < 1500:
        discount = order_amount * 0.07
        final_amount = order_amount - discount
    else:
        discount = 0
        final_amount = order_amount
    
    tax = final_amount * 0.05 + final_amount
    return final_amount, discount, tax

for amount in order_amounts:
    final_amount, discount, tax = calculate_discount(amount)
    values_after_discount = [final_amount, round(discount, 2), tax, round(tax - final_amount, 2)]
    print(f"{amount}: {values_after_discount}")

count = 0
for amount in order_amounts:
    final_amount, discount, tax = calculate_discount(amount)
    
    if discount == 0:
        count += 1
        
print(f"Number of orders with no discount: {count}")