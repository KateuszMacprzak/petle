a=['1','2']
b=['00','15','30','45']
x=0
y=0
for i in a:
    for j in b:
        print(a[x],":",b[y],"PM")
        y+=1
    x+=1
    y=0
