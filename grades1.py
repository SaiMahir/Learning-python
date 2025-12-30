a = int(input("enter a number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))
e = int(input("enter fifth number: "))

if a > 100 or b > 100 or c > 100 or d > 100 or e > 100:
    print("invalid entry")
elif a < 0 or b < 0 or c < 0 or d < 0 or e < 0:
    print("invalid entry")
else:
    sum = a + b + c + d + e
    avg = sum / 5

    if avg in range (90,101):
        print("Grade O")
    elif avg in range (80,90):
        print("Grade A+")
    elif avg in range (70,80):
        print("Grade A")
    elif avg in range (60,70):
        print("Grade B+")
    elif avg in range (50,60):
        print("Grade B")
    elif avg in range (40,50):
        print("Grade C")
    elif avg in range (30,40):
        print("Grade D")
    else:
        print("Grade F")