
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


#A value error will occur if you put a letter (a-z) or a decimal number (10.4)
#A zero division error will occur if the user attempts to define 0 as the denomonator
#It could be possible to specify "enter a denominator greater than 0" and then force repeats of the prompt until satisfied
