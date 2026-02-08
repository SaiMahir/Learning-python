lst = [1,2.0,3,'four',(5,6),[7,8]]
tuple_count = 0
for item in lst:
    if type(item) == tuple:
        print("tuple exists")
        exit()
print("tuple doesnt exist")
        