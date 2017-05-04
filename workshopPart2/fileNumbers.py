
inFile = open("numbers.txt", mode = "r")
sum = 0
for line in inFile:
    number = int(line)
    sum += number
print(sum)
inFile.close()