x = 1
y = 0
print('Proszę wprowadzić kolejną wartość.')
print('Jeżeli wprowadzisz 0 to kończymy procedurę.')
while x !=0:  # pętla działa dopuki wprowadzany x nie równa się zero
    print ('Curent Sum',y) #drukuje sume zgodnie z: y=x+y
    x = float(input('Wprowadź wartość:')) # wprowadzanie wartości

    y += x     # y=x+y
print ('''Procedura zatrzymana.
Łączna wartość wprowadzonych liczb to:''', y)