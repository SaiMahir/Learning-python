n = int(input("enter the number of elements: "))
lst = []

for i in range (n):
    lst.append(int(input("enter element:")))

tup = tuple(lst)
print("the tuple is:", tup)