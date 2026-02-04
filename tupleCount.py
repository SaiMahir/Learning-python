l = [1,2,3,(4,5),6,(7,8,9)]
count = 0
for i in l:
    if type(i) == tuple:
        count += 1
print("Number of tuples in the list:", count)