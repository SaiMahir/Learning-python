'''n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
l1 = []
for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input("Enter element: ")))
    l1.append(a)

l2 = []
for i in range (n):
    b = []
    for j in range (m):
        b.append(int(input("enter element for second matrix:")))
    l2.append(b)

result = []
for i in range (n):
    c = []
    for j in range (m):
        c.append(l1[i][j] + l2[i][j])
    result.append(c)

print("Resultant Matrix is",result)'''

n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
l1 = []
l2 = []
for i in range (n):
    a = map(int, input("enter the elements of row"+str(i+1)+":").split())
    l1.append(list(a))

for i in range (m):
    b = map(int, input("enter the elements of row in second matrix"+str(i+1)+":").split())
    l2.append(list(b))

result = [[l1[i][j] + l2[i][j] for j in range(m)] for i in range(n)]
print("Resultant Matrix is:", result)