def palindrome(n):
   

    a = n

    b = str(a)

    rev_n = b[::-1]

    if b == rev_n:
        print(n, "is a palindrome number")
    else:
        
        return (palindrome(n+1))

n = int(input("enter a number:"))
palindrome(n)