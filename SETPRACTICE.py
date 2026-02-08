#WAP to count the unique numbers or unique elements in a list.(use set)
'''l = [1,2,3,4,5,1,2,3,4,5,6,7,8,9]
s = set(l)
count = len(s)
print("Number of unique elements in the list:", count)'''
#WAP to find the common elements between two lists.
'''l = [1,2,3,4,5,6]
l1 = [4,5,6,7,8,9]
s = set(l)
s1 = set(l1)
common_elements = s.intersection(s1)
print("Common elements between two lists:", list(common_elements))'''
#WAP to remove duplicate elements in a list.
'''l = [1,2,3,4,5,1,2,3,4,5,6,7,8,9]
s = set(l)
l = list(s)
print(l)'''
#WAP to check two lists having common elements.
'''l = [1,2,3,4,5,6]
l1 = [7,8,9,10]
s = set(l)
s1 = set(l1)
common = s.intersection(s1)
if len(common) > 0:
    print("Lists have common elements.")
else:
    print("Lists do not have common elements.")'''
#WAP to find the symmetric difference of two lists.
'''l = [1,2,3,4,5]
l1 = [4,5,6,7,8]
s = set(l)
s1 = set(l1)
sym = s.symmetric_difference(s1)
print(sym)'''
#WAP to convert list of lists into set of tuples.
'''l = [[1,2], [3,4], [5,6]]
s = set()
for i in l:
    s.add(tuple(i))
print("Set of tuples:", s)'''
#WAP to convert all list of tuples into a set .
"""l = [(1,2), (3,4), (5,6), (1,2)]
s =set()
for i in l:
    s.add(i)
print(s)"""
#WAP to remove duplicate tuples in a list using set.
'''l = [(1,2), (3,4), (5,6), (1,2)]
s = set(l)
l = list(s)
print(l)'''
#WAP to convert tuple of tuples into a set.
'''l = ((1,2), (3,4), (5,6), (1,2))
s = set()
for i in l:
    s.add(i)
print( s)'''
#WAP to replace all negetive numbers in a set with 0.
'''l = {1, -2, 3, -4, 5, -6}
l1 = set()
for i in l:
    if i < 0:
        l1.add(0)
    else:
        l1.add(i)
print(l1)'''
#WAP to seperate even numbers and odd numbers from a set where
#even numbers should be displayed should be displayed in a 
# list and odd numbers should be displayed in a tuple.
'''l = {1,2,3,4,5,6,7,8,9}
even_numbers = []
odd_numbers = []
for i in l:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(even_numbers)
print(tuple(odd_numbers))'''
#WAP to seperate +ve -ve 0 values from a set.
'''l = {1, -2, 0, 3, -4, 5, -6}
p = set()
n = set()
z = set()
for i in l:
    if i > 0:
        p.add(i)
    elif i < 0:
        n.add(i)
    else:
        z.add(i)
print(p)
print(n)
print(z)'''
#WAP to count the charecters in a string in a set.
'''s ={'one', 'two', 'three', 'four', 'five'}
s1 = set()
for i in s:
    length = len(i)
    s1.add((i, length))
print(s1)'''
'''s = {1,2,3,4,5}
s1 ={'one', 'two', 'three', 'four', 'five'}
s = list(s)
s = sorted(s)
print(s)
s1 = list(s1)
s1 = sorted(s1)
print(s1)
s2 = set()
n = len(s)
for i in range(n):
    s2.add((s[i], s1[i]))
print(s2)'''
'''l = [(1,2), (3,4), (5,6), (1,2)]
l1 = []
for i in l:
    if i in l1:
        continue
    else:
        l1.append(i)
l = l1
print(l1)'''
l = {'hello','blqrw', 'pythn'}
l = list(l)
l1 = []
print(l)
for i in l:
    if 'a' or 'e' or 'i' or 'o' or 'u' in i:
        continue
    else:
        l1.append(i)

print(l1)

