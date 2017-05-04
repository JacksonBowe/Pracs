

def main():
    numbers = []

    for i in range(0, 5):
        number = int(input('Number: '))
        numbers.append(number)
        i += 1


    print('The first number is ' + str(numbers[0]))
    print('The last number is ' + str(numbers[-1]))
    print('The smallest number is ' + str(min(numbers)))
    print('The largest number is ' + str(max(numbers)))
    print('The average of the numbers is ' + str(sum(numbers)/len(numbers)))


main()