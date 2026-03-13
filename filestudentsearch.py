with open("student.txt","r") as f:
    search = int(input("Enter roll to search: "))

    for line in f:
        record = eval(line)   # convert string to dictionary

        if record["roll"] == search:
            print("Record Found:", record)
            break
    else:
        print("Record not found")