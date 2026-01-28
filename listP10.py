l = list(map(int, input("Enter elements of l: ").split()))
l1 = list(map(int, input("Enter elements of l1: ").split()))

l2 = []

for i in l:
    if i in l1 and i not in l2:
        l2.append(i)

print("Common elements are:", l2)
