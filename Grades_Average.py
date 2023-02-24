# Sol:1 

#Welcome note
print("Welcome to the Average Calculator App\n")

#User input for name and grade
name = input("What is your name: ").title().strip()
grades_count = int(input("How many grades would you like to enter: "))

#creating user grades and appending to empty list
result = []
for i in range(grades_count):
    i = int(input('Enter grade: '))
    result.append(i)

#sorting in descending order from highest to lowest
result.sort(reverse=True)
print("\nGrades Highest to lowest:")
for i in result:
    print(f"\t{i}")

#diplaying grade summary with min, max, average
average = sum(result)/len(result)

print(f"\n{name}'s Grade Summary:")
print(f"\tTotal Number of Grades: {len(result)}")
print(f"\tHighest Grade: {max(result)}")
print(f"\tLowest Grade: {min(result)}")
print(f"\tAverage: {round(average,2)}\n")

# user input of desired average
desired_average = float(input("What is your desired average: ")) 

print(f"\nGood Luck {name}!")

# computing score to gain in next assignment
# score = highest - lowest + desired_average
# score = max(result) - min(result) + desired_average   #First method

score = (len(result)+1) * desired_average - sum(result)     #second method

print(f"You will need to get a {score} on your next assignment to earn a {desired_average} average.")
print("\nLet's see what your average could have been if you did better/worse on an assignment.")

new_results = result.copy()

#grade change from previous grades
grade_change = int(input("What grade would you like to change: "))
new_grade_change = int(input(f"What grade would you like to change {grade_change} to: "))

new_results.remove(grade_change)
new_results.append(new_grade_change)

# New grades
new_results.sort(reverse=True)
print("\nNew Grades Highest to lowest:")
for j in new_results:
    print(f"\t{j}")

#diplaying Mike's grade summary
new_average = sum(result)/len(result)

print(f"\n{name}'s Grade Summary:")
print(f"\tTotal Number of Grades: {len(result)}")
print(f"\tHighest Grade: {max(result)}")
print(f"\tLowest Grade: {min(result)}")
print(f"\tAverage: {round(new_average,2)}\n")

#Displaying results
print(f"Your new average would be a {new_average} compared to your real average of {average}!")
print(f"That is a change of {round(new_average-average,2)} points!")

#Displaying final list of results
print(f"\nToo bad your original grades are still the same!\n{result}\nYou should go ask for extra credit!")