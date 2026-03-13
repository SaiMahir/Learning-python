n = int(input("Enter a number: "))
ls = [1,2,3,4,5,6,7,8,9]

l = 0
h = len(ls) - 1 

'''while l <= h:
    mid = (l + h) // 2

    if n == ls[mid]:
        print("Element found at index", mid)
        break
    elif n < ls[mid]:
        h = mid - 1
    else:
        l = mid + 1
else:
    print("Element not found")'''
 
def binary(ls,l,h,n):
    mid = (l+h)//2
    if l>h:
        return -1
    elif n == ls[mid]:
        print("element found at index", mid)
    elif n < ls[mid]:
        return binary(ls,l,mid-1,n)
    elif n > ls[mid]:
        return binary(ls,mid+1,h,n)

print(binary(ls,l,h,n))