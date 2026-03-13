student = {}
student['name'] = input("Enter name: ")
student['roll'] = int(input("Enter roll: "))
student['grade'] = input("Enter grade: ")
student['section'] = input("Enter section: ")
student['semester'] = input("Enter semester: ")

with open("student.txt", "a") as file:
    file.write(str(student) + "\n")
with open("student.txt", "r") as file:
    print(file.read())
