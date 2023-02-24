
# Sol: 1
print("Welcome to the Grade Sorter App")

# User input of grades
first_grade = int(input("\nWhat is your first grade (0-100): "))
second_grade = int(input("What is your second grade (0-100): "))
third_grade = int(input("What is your third grade (0-100): "))
fourth_grade = int(input("What is your fourth grade (0-100): "))

# storing grades in list (mutable)
grades = [first_grade, second_grade, third_grade, fourth_grade]

print("\nYour grades are: ", grades)

# sorting grades in descending order
output = sorted(grades, reverse=True)

print(f"\nYour grades from highest to lowest are: {output}")

# Removing lowest grades
print("\nThe lowest grades will now be dropped.")
lower_1 = int(input("Removed grade: "))
lower_2 = int(input("Removed grade: "))

# Deleting lowest grades from output list
del output[-2 :]
        
output = output.remove(lower_1)
output = output.remove(lower_2)

# Printing remaining grades
print("\nYour Remaining grades are: ", output)

# Printing higest grade
print(f"Nice Work!\tYour highest grade is a {max(output)}")


