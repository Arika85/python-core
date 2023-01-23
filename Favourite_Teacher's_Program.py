# Sol 1:

# Welcome note
print("Welcome to the Favorite Teachers Program\n")

# user inputs of teachers
first = input("Who is your first favorite teacher: ").capitalize().strip()
second = input("Who is your second favorite teacher: ").title().strip()
third = input("Who is your third favorite teacher: ").capitalize().strip()
fourth = input("Who is your fourth favorite teacher: ").title().strip()

teachers = []
teachers.append(first)
teachers.append(second)
teachers.append(third)
teachers.append(fourth)

# diplaying teachers in rank order
print(f"\nYour favorite teachers ranked are: {teachers}")

# sorting teachers and diplaying teachers in alphabetical order
print(f"Your favorite teachers alphabetially are: {sorted(teachers)}")

#sorting teachers in reverse order
print(f"Your favorite teachers in reverse alphabetical order are: {sorted(teachers, reverse = True)}")

print(f"\nYour top two teachers are: {first} and {second}")
print(f"Your next two favorite teachers are: {third} and {fourth}")
print(f"Your last favorite teacher is: {fourth}")
print(f"You have a total of {len(teachers)} favorite teachers.\n")

# adding new teacher
new_teacher = input(f"Oops, {first} is no longer your first favorite teacher. Who is your new FAVORITE teacher: ").capitalize().strip()
teachers.insert(0, new_teacher) 

print(f"\nYour favorite teachers ranked are: {teachers}")

# sorting teachers and diplaying teachers in alphabetical order
print(f"Your favorite teachers alphabetially are: {sorted(teachers)}")

#sorting teachers in reverse order
print(f"Your favorite teachers in reverse alphabetical order are: {sorted(teachers, reverse = True)}")


print(f"\nYour top two teachers are: {teachers[0]} and {teachers[1]}")
print(f"Your next two favorite teachers are: {teachers[2]} and {teachers[3]}")
print(f"Your last favorite teacher is: {teachers[-1]}")
print(f"You have a total of {len(teachers)} favorite teachers.\n")

#removing teacher from list
remove_teacher = input("You've decided you no longer like a teacher. Which teacher would you like to remove from your list: ").capitalize().strip()
teachers.remove(remove_teacher)

print(f"\nYour favorite teachers ranked are: {teachers}")

# sorting teachers and diplaying teachers in alphabetical order
print(f"Your favorite teachers alphabetially are: {sorted(teachers)}")

#sorting teachers in reverse order
print(f"Your favorite teachers in reverse alphabetical order are: {sorted(teachers, reverse = True)}")

print(f"\nYour top two teachers are: {teachers[0]} and {teachers[1]}")
print(f"Your next two favorite teachers are: {teachers[2]} and {teachers[3]}")
print(f"Your last favorite teacher is: {teachers[-1]}")
print(f"You have a total of {len(teachers)} favorite teachers.\n")

# Sol 2:
[14:55, 07/11/2022] Shubham 360: print("Welcome to Favorite Teachers Program")

teacher_list = []

first = str(input("\nWho is your first favorite teacher: "))
second = str(input("Who is your second favorite teacher: "))
third = str(input("Who is your third favorite teacher: "))
fourth = str(input("Who is your fourth favorite teacher: "))

# appending list
teacher_list.append(first)
teacher_list.append(second)
teacher_list.append(third)
teacher_list.append(fourth)

# ranking
print(f"\nYour favorite teachesr rank is: {teacher_list}")
print(f"Your favorite teachers rank aphabetically {sorted(teacher_list)}")
print(f"Your favorite teachers rank reverse aphabetically {sorted(teacher_list, reverse=True)}")

# pass
print(f"\nYour top two teachers are {teacher_list[0]} and {teacher_list[1]}.")
print(f"\nYour next two teachers are {teacher_list[2]} and {teacher_list[3]}.")
print(f"\nYour last favorite teachers is {teacher_list[3]}.")
print(f"You have {len(teacher_list)} favorite teachers.")

# pass
new_teacher = str(input(f"\nOops, {first} is no longer your first favorite teacher. Who is you new FAVORITE teacher:"))

teacher_list.append(new_teacher)

print(f"\nYour favorite teachesr rank is: {teacher_list}")
print(f"Your favorite teachers rank aphabetically {sorted(teacher_list)}")
print(f"Your favorite teachers rank reverse aphabetically {sorted(teacher_list, reverse=True)}")

# pass
print(f"\nYour top two teachers are {teacher_list[0]} and {teacher_list[1]}.")
print(f"\nYour next two teachers are {teacher_list[2]} and {teacher_list[3]}.")
print(f"\nYour last favorite teachers is {teacher_list[3]}.")
print(f"You have {len(teacher_list)} favorite teachers.")

dislike_teacher = str(input('You\'ve decided you no longer like a teacher. Which teacher wound u like to remove from your list: '))
teacher_list.remove(dislike_teacher)

print(f"\nYour favorite teachesr rank is: {teacher_list}")
print(f"Your favorite teachers rank aphabetically {sorted(teacher_list)}")
print(f"Your favorite teachers rank reverse aphabetically {sorted(teacher_list, reverse=True)}")

# pass
print(f"\nYour top two teachers are {teacher_list[0]} and {teacher_list[1]}.")
print(f"\nYour next two teachers are {teacher_list[2]} and {teacher_list[3]}.")
print(f"\nYour last favorite teachers is {teacher_list[3]}.")
print(f"You have {len(teacher_list)} favorite teachers.")












 


