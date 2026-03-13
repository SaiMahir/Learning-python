'''file = open("test.txt","r")
count = 0
for i  in file:
    for j in i:
            count += 1
print(count)
file.close()'''
file = open("test.txt","w+")
file.write("hellow world")
file.seek(0)
print(file.read())
file.close()
