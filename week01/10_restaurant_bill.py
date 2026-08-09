food_price = int(input("Enter food price"))
tax_percentage = float(input("Enter tax percentage: "))
discount_percentage = float(input("Enter discount percentage: "))
fixed_service_chrages = float(input("Enter fixed service charges: "))

amount = food_price + (food_price * tax_percentage / 100)
amount = amount - (amount * discount_percentage / 100)
amount = amount + fixed_service_chrages

print(f"Final bill: {amount:.2f}")