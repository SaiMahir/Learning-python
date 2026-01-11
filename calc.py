def calculator():
    sign = input ("enter an operation: ")
    a = int(input("enter a number:"))
    b = int(input("enter a number:"))
    
    if sign == "+":
        sum = a+b
        print(sum)
    elif sign == "-":
        sum = a-b
        print(sum)
    elif sign == "*":
        sum = a*b
        print(sum)
    elif sign == "/":
        sum = a/b
        print(sum)
    else:
        print("wrong operator input")
    
calculator()