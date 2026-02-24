students = [{"name": "Alice", "age": 20, "grade": "A"},
            {"name": "Bob", "age": 22, "grade": "B"},
            {"name": "Charlie", "age": 21, "grade": "A"},]
n = input("Enter name of student to delete: ")
for i in students:
    if i['name'] == n:
        students.remove(i)
        print("Student deleted:", i)
        exit()