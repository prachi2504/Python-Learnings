order_amount = int(input("Enter the order amount: "))

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
    return final_amount, discount

# Adding Tax of 5% to the final amount
final_amount, discount = calculate_discount(order_amount)
tax = final_amount * 0.05 + final_amount

print(f"Discount: {discount}")
print(f"Tax Amount: {tax - final_amount}")
print(f"Sub Total Amount: {final_amount}")
print(f"Final Amount: {tax}")
