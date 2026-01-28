n = int(input("enter no of rows:"))
m = int(input("enter no of columns:"))
matrix = []
'''for i in range (n):
    lst = []
    for j in range (m):
        lst.append(0)
    matrix.append(lst)'''
result = [[0 for j in range(m)] for i in range(n)]

print("matrix is :", result)