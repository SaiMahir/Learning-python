a = int(input("enter a number: "))
rev = 0
temp = a
while temp>0:
    digit = temp%10
    rev = rev*10 + digit
    temp//=10
if rev == a:
    print(a,"is a pallendrome number")
else:
    print(a,"is not a pallendrome number")
    
