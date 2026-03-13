with open("student.txt", "r") as file:
    count = 0
    for i in file:
        count += 1
print("Number of students:", count)