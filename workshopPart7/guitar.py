from Guitars import Guitar


def main():
    name = input("Name: ")
    guitar_list = []
    while name.strip("") != "":
        year = int(input("Year: "))
        cost = float(input("Cost $"))
        guitar = Guitar(name, year, cost)
        guitar_list.append(guitar)
        print('{} added.'.format(guitar))
        name = input("Name: ")

    i = 1

    for item in guitar_list:
        vintage_string = item.is_vintage()
        print('Guitar {}: {:>20} ({}), worth ${:10,.2f} {}'.format(i, item.name, item.year, item.cost, vintage_string))
        i += 1


main()
