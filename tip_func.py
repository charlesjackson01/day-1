def total_with_tip(bill, percent):
    return bill + bill * percent / 100

total = total_with_tip(50, 20)

print(f"Total: ${total}")