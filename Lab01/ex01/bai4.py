a=[]
for i in range(1999,3201):
    if (i %7==0) and (i % 5!=0):
        a.append(i)
print(a)