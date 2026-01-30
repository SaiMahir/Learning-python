tup = tuple(map(int, input("enter elements:").split()))
l = list(tup)
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        print("repeated element is:", i)