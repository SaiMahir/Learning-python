l = list(map(int, input("enter elments of l:").split()))
l1 = list(map(int,input ("enter elements of list1:").split()))

l2 = []
for i in range(len(l)):
    for j in range(len(l1)):
        if l[i] == l1[j]:
            l2.append(l[i])

print("common elements are :", l2)