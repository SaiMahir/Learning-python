my_list = [1,2,3,4,5,6,7,8,9,10]
print("Length:", len(my_list))
print("Max:", max(my_list))
print("Min:", min(my_list))
print("Sum:", sum(my_list))
print("Sorted (reverse):", sorted(my_list, reverse=True))

my_list.remove(5)
print("After remove(5):", my_list)

print("Reversed:", list(reversed(my_list)))

my_list.insert(2, 15)
print("After insert(2,15):", my_list)

print("Count of 3:", my_list.count(3))

print("Index of 4:", my_list.index(4))

my_list.sort()
print("After sort():", my_list)

popped = my_list.pop()
print("Popped element:", popped)
print("After pop():", my_list)

my_list.extend([11,12,13])
print("After extend([11,12,13]):", my_list)

my_list.clear()
print("After clear():", my_list)
