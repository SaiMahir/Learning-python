l = list(map(int, input("enter elements:").split()))
print(l)
for i in range (len(l)):
    if l[i] == 0:
        l.pop(i)
        l.append(0)
        i = i - 2
    
print(l)