n = int(input("enter number of rows:"))
m = int(input("enter number of columns:"))
l1 = []
for i in range(n):
    a = map(int, input("enter the elements of row "+str(i+1)+":").split())
    l1.append(list(a))
l2 = []
for i in range(n):
    b = map(int, input("enter the elements of row "+str(i+1)+" for second matrix:").split())
    l2.append(list(b))
result = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        for k in range(m):
            result[i][j] += l1[i][k] * l2[k][j]
print("Resultant Matrix is:", result)