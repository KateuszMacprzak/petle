b=0 #ta zmienna ma przechowywać ilość wprowadzonych 5 
for x in range(6):
    a=input('Wprowadz liczbe od 1 do 10: ')
    a=int(a)
    if (a==5):
        b+=1
print('Ilość wprowadzonych 5: ',b)
    