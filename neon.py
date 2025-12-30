a = int(input("enter a number:"))
n = a**2
sum = 0

while n>0:
    digit = n%10
    sum  = digit + sum
    n//=10

if sum == a:
    print(a, "is a neon number")
else:
    print(a, "is not a neon number")