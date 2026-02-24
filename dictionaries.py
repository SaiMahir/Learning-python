'''d = {1:'one', 2:'two', 3:'three'}
print(d.keys())
print(d.values())
print(d)'''
"""n = int(input("Enter number of students: "))
d = {}
for i in range(n):
    key = int(input("Enter pin: "))
    value = input("Enter name: ")
    d[key] = value
print("Dictionary:", d)"""
l = [1,2,3,4,5,6]
l1 = ["one", "two", "three", "four", "five", "six"]
d = {}
for i in range(len(l)):
    d[l[i]] = l1[i]
print(d)