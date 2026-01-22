#A lambda function is a small, one-line function defined using the lambda keyword instead of def.
n = int(input("Enter a number: "))
p = int(input("enter a number: "))

sqr = lambda x: x*x
add = lambda x,y : x+y
sub = lambda x,y: x-y
multiply = lambda x,y: x*y
divide = lambda x,y: x/y
gi = lambda x,y: max(x,y)
print(sqr(n))
print(add(n,p))
print(sub(n,p))
print(multiply(n,p))
print(divide(n,p))
print(gi(n,p))