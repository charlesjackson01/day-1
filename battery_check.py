battery_percent = float(input("What's the battery percent?"))

if battery_percent < 20:
    print("Plug in now")
else:
    print("Battery fine")