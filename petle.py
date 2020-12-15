import random
imie=random.choice(['Ewa','Mateusz','Natalia','Michał'])
dlugosc=len(imie)
if (imie[-1]=='a'):
    print('To imię damskie !')
else:
    print('To imię męskie !')
print(dlugosc)
a=input('Spróbuj zgadnąć to imię: ')
x=0
while(a!=imie):
    x+=1
    print('Nie udało Ci się zgadnąć, to Twoja', x, 'próba')
    a=input('Spróbuj zgadnąć to imie: ')
else:
    print('Gratulacje, udało Ci się wygrać ! To była Twoja ',x,' próba')
