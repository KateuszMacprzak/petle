def funkcja():
    a=input('Proszę wcisnąć literę n lub c: ')
    if (a=='n'):
        print('Dziękuje !')
    elif (a=='c'):
        print('Dziękuje !')
    elif (a!='n' or a!='c'):
        funkcja()
print('Witaj w programie :)')
funkcja()