COLOUR_NAMES = {'YELLOW1': '#ffff00', 'VIOLET': '#ee82ee', 'BLUE1': '#000ff', 'DARKGREEN': '#006400',
                'CYAN1': '#00ffff', 'DARKORANGE': 'ff8c00', 'WHITE': '#fffff', 'WHEAT': '#f5deb3', 'THISTLE': '#d8bfd8',
                'TAN': '#d2b48c'}

print(COLOUR_NAMES)

colour = input("Enter a colour name: ").upper()
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter a colour name: ").upper()