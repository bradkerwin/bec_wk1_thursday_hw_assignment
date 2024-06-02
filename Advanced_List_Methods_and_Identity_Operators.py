# Task 1:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
for student in attended:
    if student in submitted:
        print(student)

# Task 2:
print(submitted is attended) # returns False as the lists are not identical.

# Task 3:
attended.remove("Eve")
attended.remove("Frank")
print(attended)
