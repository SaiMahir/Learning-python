students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 21, "grade": "A"},
            ]

search_name = input("Enter name to search: ")
for i in students:
    if i["name"] == search_name:
        print("Student found:", i)
        exit()
print("Student not found")