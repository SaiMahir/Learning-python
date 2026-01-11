n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

count_dict = {}

for item in lst:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)


