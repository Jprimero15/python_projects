print("Simple Offline PHP currency converter!\n(Currenly supported: USD, AUD, EUR)")

choice = str(input("Type your currency:")).lower()
amount = float(input("Amount:"))

if choice == "usd":
 new_amount = amount * 62.27
 print(f"{new_amount} php")
elif choice == "aud":
 new_amount = amount * 44.62
 print(f"{new_amount} php")
elif choice == "eur":
 new_amount = amount * 72.44
 print(f"{new_amount} php")
else:
 print("Invalid currency! Try again")
