from programminglanguage import ProgrammingLanguage

def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    list = [ruby, python, vb]

    dynamics = []
    for i in list:
        if i.typing == 'Dynamic':
            dynamics.append(i.language)

    if len(dynamics) > 0:
        print('The dynamically typed languages are:')
        for j in dynamics:
            print(j)
    else:
        print('No dynamic languages')





main()