score = float(input("Enter score"))
if 0 > score > 100:
    print("Invalid score")
elif 50 < score < 90:
    print("Passable")
elif score > 90:
    print("Excellent")
else:
    print("Bad")