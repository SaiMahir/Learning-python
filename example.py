n = int(input("enter the number you want to search:"))
l = list(map(int, input("enter elements:").split()))
if n in l:
    print(n, "is present in the list")
else:
    print(n, "is not present in the list")