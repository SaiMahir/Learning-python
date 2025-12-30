
# Program to check Armstrong Number

num = int(input("Enter a number: "))
temp = num
sum = 0

# Find number of digits
digits = len(str(num))

# Calculate sum of digits raised to power
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

# Check Armstrong condition
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
