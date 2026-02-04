l = list(map(int,input("enter the elements:").split()))
l2 = []

for i in range (len(l)):
    if  l[i]%2 == 0 :
        continue
    else:
        l2.append(l[i])

print(l2)
