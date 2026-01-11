def prime(n):
    for i in range(1,n+1):
        if n%i == 1:
            print(i)
        else:
            return prime(n)

n = int(input("enter a number:"))
prime(n)