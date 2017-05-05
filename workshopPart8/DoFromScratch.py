from workshopPart8.Inheritance import SilverServiceTaxi
from workshopPart8.Inheritance import Taxi

def main():

    MENU = 'q)uit, c)hoose taxi, d)rive'
    print('Lets drive!\n' + MENU)
    choice = input('>>>').upper()
    taxis = [Taxi('Prius', 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    taxichoice = []
    total_cost = 0.00
    while choice != 'Q':
        if choice == 'C':
            print('Taxis available:')
            i = 0
            for taxi in taxis:
                print('{} - {}'.format(i, taxi))
                i += 1
            taxichoice = int(input('Choose taxi: '))
            print('Bill to date: ${}'.format(total_cost))

        elif choice == 'D':
            if taxichoice != []:
                drive_distance = int(input('Drive how far? '))
                taxis[taxichoice].drive(drive_distance)
                print('Your {} trip costs you ${}'.format(taxis[taxichoice].name, taxis[taxichoice].get_fare()))
                total_cost += taxis[taxichoice].get_fare()
                print('Bill to date: ${}'.format(total_cost))

            else:
                print('Please select a taxi')
        print(MENU)
        choice = input('>>>').upper()

    print('Total trip cost: ${}'.format(total_cost))
    print('Taxis are now:')
    for taxi in taxis:
        print('{} - {}'.format(i, taxi))
        i += 1














main()