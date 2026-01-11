n = int(input("eneter the number of elements:"))
lst = []
lst_sqr = []

for i in range (n):
    lst.append(int(input("enter element:")))

print(lst)

for i in lst:
    lst_sqr.append(i**2)

print("the square of the elements are:", lst_sqr)