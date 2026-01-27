l = list(map(int, input("enter elements:").split()))
print(l)
l1 = list(map(int, input("enter sublist elements:").split()))

n = len(l)
l.remove(l[n-1])
l.append(l1)
print("list after adding sublist is :", l)
    

