print("Simple Offline PHP currency converter!\n(Currenly supported: USD, AUD, EUR)")

def compute():
    print(f"{new_amount:,.2f} php")

choice = str(input("Type your currency:")).lower()
amount = float(input("Amount:"))

if choice == "usd":
    new_amount = amount * 62.27
    compute()
elif choice == "aud":
    new_amount = amount * 44.62
    compute()
elif choice == "eur":
    new_amount = amount * 72.44
    compute()
else:
    print("Invalid currency! Try again")
