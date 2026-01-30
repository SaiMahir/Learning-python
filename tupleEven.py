tup = tuple(map(int, input("enter elements:").split()))
l = []
for i in tup :
    if i%2 == 0 :
        l.append(i)
tup = tuple(l)
print(tup)