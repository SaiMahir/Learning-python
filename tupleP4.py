t = [(1,2), (3,4), (5,)]
t1 = []
for i in t:
    for j in i:
        t1.append(j)

print("Flattened tuple as list:", t1)
