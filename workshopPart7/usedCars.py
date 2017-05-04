from car import Car

def main():
    bus = Car(180, 'bus')
    bus.drive(30)
    print(bus)

    limo = Car(180, "limo")
    limo.add_fuel(20)
    limo.drive(115)
    print(limo)


main()