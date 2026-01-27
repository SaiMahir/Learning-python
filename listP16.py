l = list(map(int, input("Enter values in the list: ").split()))
l2 = []

for i in l:
    if i not in l2:
        count = 0
        for j in l:
            if i == j:
                count += 1
        l2.append(i)
        print(i, "appears", count, "times")