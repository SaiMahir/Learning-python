l = [1,2,3,(4,5),6,(4,5)]
l1 = []
count = 0
for i in l:
    if type(i) == tuple:
        count += 1

for i in l:
    if i not in l1 and type(i) == tuple:
        l1.append(i)
    else:
        l.pop(i)
print("Number of tuples in the list:", count)