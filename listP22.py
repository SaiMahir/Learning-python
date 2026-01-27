l = list(map(int, input("enter elements:").split()))

for i in range(len(l)-1, 0, -1):
    print(i)
    if l[i] == l[i-1]:
        l.pop(i)

print(l)