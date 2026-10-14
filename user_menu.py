print("Welcome to the Order Management System")
print("Menu:")
print("1. Add order amount to the List")
print("2. Show all orders and total after applying discount")
print("q. Quit")
user_input = str(input("Enter the value from 1,2 and q to open the Menu : "))
user_order_list = []

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


while user_input != 'q':
    if user_input == '1':
        order_amount = input("Enter the value from Menu: ")
        user_order_list.append(order_amount)
        print("Order amount added to the list.")
    elif user_input == '2':
        if not user_order_list:
            print("No orders in the list.")
            continue
        print("Order Amounts:", user_order_list)
        print("Calculating discounts for the orders...")
        for amount in user_order_list:
            final_amount, discount = calculate_discount(float(amount))
            print(f"Order Amount: {amount}, Final Amount: {final_amount}, Discount: {discount}")
    elif user_input == 'q':
        print("Quitting the program.")
        break
    else:
        print("Invalid input. Please try again.")
        continue
    user_input = str(input("Enter the value from 1,2 and q to open the Menu : "))
