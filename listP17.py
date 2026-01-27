l = list(map(str, input("enter strings:").split()))
l1 = input("enter the sentence:")
for i in (l):
    if i in l1:
        print(i, "is present in the sentence")
    else:
        print(i, "is not present in the sentence")