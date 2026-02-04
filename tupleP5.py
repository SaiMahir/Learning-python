n = int(input("Enter number: "))
l = [1,[1,2],(1,2,6), (3,4), (5,6)]
l1 = []
for i in l:
    if type(i) != tuple:
        l1.append(i)
    else:
        temp = list(i)      
        temp.pop()          
        temp.append(n)     
        l1.append(tuple(temp))  
l = l1
print(l)
    
