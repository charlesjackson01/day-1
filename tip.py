bill = float(input("Bill amount:"))

tip_percent = float(input("Tip percent:"))

tip = bill * tip_percent / 100

total = bill + tip

print(f"Tip: ${tip}")
print(f"Total: ${total}")