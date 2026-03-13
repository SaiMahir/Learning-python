search = int(input("Enter roll to delete: "))
lines = []

with open("student.txt","r") as f:
    for line in f:
        record = eval(line)

        if record["roll"] != search:
            lines.append(line)
        else:
            print("Record Deleted:", record)

with open("student.txt","w") as f:
    f.writelines(lines)