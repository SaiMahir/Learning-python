file = open("student.txt","w+")
n = int(input("Enter number of students: "))
lst = []

for i in range(n):
    d = {}
    name = input("Enter name: ")
    roll = int(input("Enter roll: "))
    grade = input("Enter grade: ")
    sec = input("Enter section: ")
    sem = input("Enter semester: ")
    d = {"name": name,
         "roll": roll,
         "grade": grade,
         "section": sec,
         "semester": sem}
    lst.append(d)
for i in lst:
    file.write(str(i) + "\n")
file.seek(0)
print(file.read())
file.close()