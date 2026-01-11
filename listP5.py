n = int(input("Enter the number of elements: "))
lst = []
lst1 = []
dic = {}

for i in range(n):
    lst.append(int(input("Enter element: ")))

for i in range (n):
    lst1.append(int(input("Enter element for lst 1: ")))

for i in range (n):
    dic[lst[i]] = lst1[i]

print("The dictionary formed is:", dic)


