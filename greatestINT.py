a = int(input("enter a number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a>b and a>c:
    print(a, "is the greatest integer")
elif b>a and b>c:
    print(b, "is the greatest integer")
elif a==b:
    print("First and second numbers are equal and greatest")
elif b==c:      
    print("Second and third numbers are equal and greatest")
elif a==b==c:
    print("All numbers are equal")
else:
    print(c, "is the greatest integer")