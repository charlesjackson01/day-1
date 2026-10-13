price = 50

coupon = input("Coupon? (yes/no):")


if coupon == "yes":
    print(f"total is:{price * 90 / 100}")
else:
    print(f"total is:{price}")