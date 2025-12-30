n = int(input("enter a number:"))
odd_count = 0
even_count = 0

for i in range(1,n+1):
    print(i)
    if i%2 == 0:
        even_count = even_count + 1
    else:
        odd_count += 1

print("even numbers= ",even_count)
print("odd numbers= ",odd_count)