daily_sales = [200, 150, 0, 400, 50, -1, 300]

total_sale = 0
for sale in daily_sales:
    if sale < 0:
        print(f"Corrupted Data {sale}.")
        break
    elif sale == 0:
        print(f"No sales recorded for the day.")
        continue
    else:
        total_sale += sale
        print(f"Running Total Sale amount: {total_sale}")

print(f"Total Sale amount for the week: {total_sale}")