# Task 1:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

# Task 2:
grade_average = sum(grades) / len(grades)
print(grade_average)

# Task 3:
print(grades)
failing_grade1 = grades.pop(9)
grades.insert(9, "Failed")
# print(grades)
failing_grade2 = grades.pop(8)
grades.insert(8, "Failed")
# print(grades)
failing_grade1 = grades.pop(7)
grades.insert(7, "Failed")
print(grades)