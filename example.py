l = [1,2,3]
found = False
for i in l:
    if type(i) == list:
        found = True
    else:
        found = False
if found:
    print("sublist exists")
else:
    print("sublist doesnt exist")
