n = int(input("enter a number:"))

last = n % 10
first = n 

while first >= 10:
    first //= 10

sum = first + last
print("Sum of first and last digit is:", sum)

#without while loop
first_digit = int(str(n)[0])
last_digit = n % 10
sum_digits = first_digit + last_digit
print("Sum of first and last digit is:", sum_digits)