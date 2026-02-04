lst = [1,2.0,(1,2), (3,4), (5,6), (7,8,9)]
lst1= []
for i in lst:
    if type(i) == tuple:
        lst1.append(list(i))
    else:
        lst1.append(i)
lst = lst1
print("Converted tuples to lists:", lst)