liczba=input('Wprowadz wartość: ')
a=1
liczba=int(liczba)
if (liczba==0):
    print('0! wynosi 1 ')
else:
    while liczba >=1:
        a=a*liczba
        liczba=liczba-1
    print('Silnia wynosi: ',a)
