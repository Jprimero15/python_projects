print("Simple PHP currency converter!\n(Currenly supported: USD, AUD, EUR)")

choice = str(input("Type your currency:"))
amount = float(input("Amount:"))

if choice.lower() == "usd":
 new_amount = amount * 62.27
 print(f"{new_amount} php")
elif choice.lower() == "aud":
 new_amount = amount * 44.62
 print(f"{new_amount} php")
elif choice.lower() == "eur":
 new_amount = amount * 72.44
 print(f"{new_amount} php")
else:
 print("Invalid currency! Try again")
