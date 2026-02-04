l1 = [(1,2,3), (4,5,6), (7,)]
l = []
for i in l1:
    total = (sum(i))
    l.append(total)

print (sum(l))
print("Sum of each tuple in the list:", l)