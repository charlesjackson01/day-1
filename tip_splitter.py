bill = float(input("Bill amount:"))
tip_percent = float(input("Tip percentage:"))
tip = bill * tip_percent / 100
people = float(input("How many people?" ))
total = bill + tip
per_person = total / people

print(f"Bill: ${bill}")
print(f"Tip: ${tip}")
print(f"Total: ${total}")
print(f"Amount per person: ${per_person}")
