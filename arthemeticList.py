a = list(map(int,input("enter the elements: ").split()))
b = list(map(int,input("enter the elements: ").split()))
operator = input("Enter the operation (+, -, *, /): ")
add = []
sub = []
multiply = []
division = []
for i in range(len(a)):
    add.append(a[i]+b[i])
    sub.append(a[i]-b[i])
    multiply.append(a[i]*b[i])
    division.append(a[i]/b[i])
if operator == '+':
    print("The addition of two lists is:", add)
elif operator == '-':
    print("The subtraction of two lists is:", sub)
elif operator == '*':
    print("The multiplication of two lists is:", multiply)
elif operator == '/':
    print("The division of two lists is:", division)
else:
    print("Invalid operator")