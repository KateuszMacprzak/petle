x='ARA'
y='BereKA'
z='GONabEACH'
print('Wybierz numer wyrazu, który ma być przeliterowany ? ',x,y,z)
a=input('Podaj liczbę 1, 2 lub 3: ')
a=int(a)
if (a==1):
        for i in x:
            print(i)
if (a==2):
        for i in y:
            print(i)
if (a==3):
        for i in z:
            print(i)
        
#rozwiązanie ze strony internetowej
#a = ('ARA','BereKA','GONabEACH')
#print("To są wyrazy do wyboru:",a[0],",",a[1],",",a[2])
#
#n = int(input('''Wybierz numer wyrazu, który ma być przeliterowany? 
#    Podaj liczbę: 1, 2 lub 3: '''))
#n -=1
#print("wybrałeś słowo:",a[n])
#for s in a[n]:
#    print(s)         

