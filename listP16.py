l = list(map(int,input("enter elemnts:").split()))
l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
        count = 0
        for j in l:
            if i == j:
                count += 1
        print(i,"repeated",count)
    else:
        continue 