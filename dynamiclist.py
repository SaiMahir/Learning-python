n = int(input("Enter the number of elements: "))
dynamic_list = []
for i in range(n):
    element  = int (input("enter element:"))
    dynamic_list.append(element)

print("The dynamic list is:", dynamic_list)

even_sum= 0
odd_sum = 0
for i in range (len(dynamic_list)):
    if dynamic_list[i] % 2 == 0:
        even_sum += dynamic_list[i]
    else:
        odd_sum += dynamic_list[i]

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)