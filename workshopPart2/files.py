#Ask for name
#Create file name.txt
#Write name of user to name.txt


nameput = input("Enter your first name: ")
outFile = open("name.txt", mode = "w")
outFile.write(nameput)
outFile.close()

inFile = open("name.txt", mode = "r")
nameget = inFile.read().strip()
print("Your name is:", nameget)
inFile.close()
