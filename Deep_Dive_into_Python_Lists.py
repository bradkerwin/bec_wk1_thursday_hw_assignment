# Task 1:
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
for x in range(len(grades)):
    if grades[x] < 80:
        print(students[x], grades[x], activities[x])

# Task 2:
students_approved = []
students_approved.append(students[0])
# print(students_approved)
students_approved.append(students[1])
# print(students_approved)
students_approved.append(students[3])
print(students_approved)

# Task 3:
print(students_approved)