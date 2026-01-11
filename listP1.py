n = int(input("enter no of elements:"))
lst = []
for i in range (n):
    lst.append(int(input("enter elements:")))

lst1 = []

'''for i in range (n):
    lst1.append(lst[i])'''

'''lst1.extend(lst)'''

lst1 = lst.copy()

print('the new list:',lst1)
