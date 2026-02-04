l1 = list(map(int,input("enter values in l1:").split( )))
l2 = []

for i in (l1):
    if i in (l2):
        l1.pop(i)
    else:
        l2.append(i)
        continue
print(l1)