a = int(input("enter a number: "))
c = 0
#using while loop
while(a>0):
  
    c = c + 1
    a//=10
print("length of number is:", c)