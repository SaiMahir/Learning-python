n = int(input("enter number of values:"))
s = set()
for i in range(n):
    d1 = int(input("enter value to add to set:"))
    d2 = int(input("enter another value to add to set:"))
    s.add((d1,d2))
print("Set elements are:", s)
print(dir(set))
