#Intermediate

charChoice = input("Enter a character: ")
print("The ASCII code for " + charChoice + " is ", ord(charChoice))
#numChoice = int(input("Enter a number between 33 and 127: "))
#print("The character for " + str(numChoice) + " is ", chr(numChoice))


try:
    numChoice = int(input("Enter a number between 33 and 127: "))

    if 33 < numChoice < 127:
        print("The character for " + str(numChoice) + " is ", chr(numChoice))
    else:
        print("Number must be between 33 and 27")
except ValueError:
    print("That's not a number!")

i = 33

while 33 <= i < 127:
    chari = chr(i)
    print('{:3} {:>4}'.format(i, chari))

    i += 1