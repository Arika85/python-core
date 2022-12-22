
# Sol: 1

print("Welcome to the Grade Sorter App")

first = int(input("\nWhat is  your first grade (0-100): "))
second = int(input("What is  your second grade (0-100): "))
third = int(input("What is  your third grade (0-100): "))
fourth = int(input("What is  your fourth grade (0-100): "))

grades = [first, second, third, fourth]

print(f"\nYour grades are: {grades}")

# sorting grades in descending order

sorted_grades = sorted(grades, reverse=True)

print(f"\nYour grades from highest to lowest are: {sorted_grades}")

print("\nThe lowest two grades will be dropped.")
print(f"Removed grade: {sorted_grades.pop()}")
print(f"Removed grade: {sorted_grades.pop()}")

print(f"Your remaining grades are: {sorted_grades}")
print(f"Nice work!\tYour highest grade is a {max(sorted_grades)}")




# Sol: 2
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



# sol: 3
# welcome message
print("Welcome to Grade sorter App\n")

# user inout grade
f_grade = int(input("What is your first grade: "))
s_grade = int(input("What is your second grade: "))
t_grade = int(input("What is your third grade: "))
fo_grade = int(input("What is your fourth grade: "))

# grade list
grade_list = [f_grade, s_grade, t_grade, fo_grade]
print(f"\nYour grades are {grade_list}")

# sorting list
sorted_list = sorted(grade_list, reverse=True)
print(f"\nYour grades from highest to lowest are: {sorted_list}")

# finding lowest grades
low_1 = sorted_list.pop()
low_2 = sorted_list.pop()

# droping lowest grades
print("\n The lowest two grades will now be droped")
print(f"Removed Grade: {low_1}")
print(f"Removed Grade: {low_2}")

# printing everything
print(f"\nRemaining grades are {sorted_list}")
print(f"Nice work! Your highest grade is {sorted_list[0]}")
