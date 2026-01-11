'''WAP to count occurrences of an element in a list.
Also count number of negative elements in the list.
If element or negative elements are not found, print
("No element found" or "No negative element found")'''

n = int(input("enter a value:"))

lst = []
count = 0
neg_count = 0

for i in range (n):
    lst.append(int(input("enter the element:")))

a = int(input("enter the number to be checked:"))

for i in (lst):
    if i == a:
        count = count + 1

'''lst.count(a) can also be used to find count of a in lst'''

for i in (lst):
    if i is i<0:
        neg_count += 1

if count != 0:
    print(count)
else:
    print("no element found")

if neg_count != 0:
    print(neg_count)
else:
    print("no negative element found")