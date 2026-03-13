'''student = {}
n = int(input("Enter number of students: "))
for i in range(n):
    key = int(input("Enter pin: "))
    value = input("Enter name: ")
    student[key] = value
print("Dictionary:", student)'''
#taking input in run time and creating a dictionary
keys = []
values = []
n = int(input("Enter number of students: "))
for i in range(n):
    key = int(input("Enter pin: "))
    value = input("Enter name: ")
    keys.append(key)
    values.append(value)
d = dict(zip(keys, values))
print("Dictionary:", d)