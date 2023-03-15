from datetime import datetime

date = datetime.now()
list1 = ("meat").title().strip()
list2 = ("cheese").title().strip()

date_time = date.strftime("%m/%d %H:%M")

print("Welcome to the Grocery List App.")
print(f"Current Date and Time: {date_time}")
print(f"You currently have {list1} and {list2} in your list.")






