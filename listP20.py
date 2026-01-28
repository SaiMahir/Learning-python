l = list(map(int, input("enter elements:").split()))
print(l)
n = len(l) 
for i in range (n-1 , 0 , -1):
    if l[i] == 0:
        l.pop(i)
        l.append(0)
    
print(l)