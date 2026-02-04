n = int(input("enter number of lists u wanna enter:"))
lists = []
for i in range (n):
    lst = list(map(int,input("enter list:").split()))
    lists.append(lst)
print(lists)