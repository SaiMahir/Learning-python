n = int(input("enter the number of elements:"))
lst = []
even_lst = []
odd_lst = []

for i in range (n):
    lst.append(int(input("enter the element:")))

for i in lst:
    if i%2 ==0 :
        even_lst.append(i)
    else:
        odd_lst.append(i)

print(even_lst)
print(odd_lst)