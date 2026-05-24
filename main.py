print("Smart Study Timetable Generator")

subjects = int(input("How many subjects do you have? "))

for i in range(subjects):
    name = input("Enter subject name: ")
    hours = input("Enter study hours: ")

    print(name, "->", hours, "hours")

print("Study timetable created successfully!")