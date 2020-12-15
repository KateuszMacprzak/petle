x=input('Proszę wpisać literę n lub c: ')
i=1
def funkcja():
    while (i>0):
        a=input('Proszę wpisać literę n lub c: ')
        if (a=="n"):
            print("Dziękuje")
            break
if (x=="n" or x=="c"):
    print("Dziękuje")
else:
    print("Błąd")
    funkcja()