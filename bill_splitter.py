people = float(input("How many people?"))

bill = float(input("Bill Amount:"))

tip = float(input("Tip Amount:"))

total = bill + tip

per_person = total / people

print(f"Cost per person: ${per_person}")