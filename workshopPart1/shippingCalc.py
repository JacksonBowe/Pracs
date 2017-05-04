

MENU = "N - Enter Number of Items to be Shipped\nQ (for quit)"
MENU2 = "Y - Thank you, would you like to use again?\nQ (for quit)"
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    numItem = input("Number of Items: ")
    if int(numItem) <= 0:
        print("Invalid")
        MENU = "N - Enter Number of Items to be Shipped\nQ (for quit)"
        print(MENU)
        choice = input(">>> ").upper()
    else:
        items = int(numItem) + 1
        itemPriceTotal = 0.0
        itemPriceFinal = 0
        for i in range(1, items, 1):
            itemPrice = float(input("Price of item " + str(i) + ": "))
            itemPriceTotal += itemPrice
        if float(itemPriceTotal) > 100:
            itemPriceFinal = float(itemPriceTotal) * 0.9
            print("Total price for " + str(numItem) + " items is $" + str(itemPriceFinal) + "")
            print(MENU2)
            choice = input(">>> ").upper()
        elif float(itemPriceTotal) <= 100:
            itemPriceFinal = float(itemPriceTotal)
            print("Total price for " + str(numItem) + " items is $" + str(itemPriceFinal) + "")
            print(MENU2)
            choice = input(">>> ").upper()
        else:
            print("Invalid input")
            print(MENU2)
            choice = input(">>> ").upper()