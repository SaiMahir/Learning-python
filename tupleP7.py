lst = []

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
for i in range(m):          # rows
    lst1 = []               # create a new row
    for j in range(n):      # columns
        a = int(input(f"Enter element [{i}][{j}]: "))
        lst1.append(a)
    lst.append(tuple(lst1)) # convert row to tuple

print(lst)
