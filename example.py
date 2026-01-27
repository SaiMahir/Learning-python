l1 = []
map(int,input("enter values in l1:").split( ))
l2 = []
map(int,input("enter values in l2:").split( ))
print (l1)
print (l2)
l3 = []
for i in range (len(l1)):
    l3.append(l1[i]*l2[i])
print(l3)