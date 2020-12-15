x=1
y=0
y=int(y)
while (x>0):
    a=input('Prosze podać kolejną wartość: ')
    a=int(a)
    y+=a
    print('Obecna suma wynosi: ',y)
    if(a==0):
        print('Koniec działań. Wynik wynosi: ',y)