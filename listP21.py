l = []
n = int (input("enter no of lists:"))
for i in range (n):
    lst = list(map(int, input("enter elements of list:").split()))
    l.append(lst)
l1 = []
for i in l:
    if i in l1:
        continue
    else:
        l1.append(i)
print("list after removing duplicates is :", l1)