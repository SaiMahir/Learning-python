a = int(input("enter your marks: "))

if a in range(90, 101):
    print("O")
elif a in range (80,90):
    print("A+")
elif a in range (70,80):
        print("A")
elif a in range (60,70):
        print("B+") 
elif a in range (50,60):
        print("B")
elif a in range (40,50):
        print("C")
elif a in range (33,40):
        print("D")  
else:
        print("F")