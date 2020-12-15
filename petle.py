x=['1','2']
y=['00','15','30','45']
a=0
b=0
for i in x:
    for j in y:
        print(x[a],':',y[b], 'PM')
        b+=1
    a+=1
    b=0