n = int(input("Enter a number: "))

sum = 0
temp = n

while n > 0:
    digit = n % 10
    sum = sum + digit
    n //= 10

if temp % sum == 0:
    print("It is a Harshad number")
else:
    print("It is not a Harshad number")
