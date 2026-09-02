amount_in_usd = int(input("Enter amount in USD: "))
exchange_rate = float(input("Enter exchnage rate: "))
converted_amount = amount_in_usd * exchange_rate

print("Converted amount: ", round(converted_amount,2))
#print(f"Converted amount: {converted_amount:.2f}")