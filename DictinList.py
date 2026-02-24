'''students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "A"},
            ]
for i in students:
    print(i["name"], i["grade"])'''
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter age: "))
    grade = input("Enter grade: ")
    student = {"name": name, "roll": roll, "grade": grade}
    students.append(student)
print("Students:", students)
