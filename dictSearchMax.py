students = [{'alice': 20, "grade": 9}, {"Bob": 22, "grade": 86}, {"Charlie": 21, "grade": 80}]
max = students[0]["grade"]
for i in students:
    
    if i["grade"] > max:
        max = i["grade"]
print("highest grade:", max)