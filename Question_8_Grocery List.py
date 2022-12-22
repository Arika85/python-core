from datetime import datetime

date = datetime.now()
date_time = date.strftime("%m/%d  %H:%M")

grocery_list = ['Meat', 'Cheese']

print("Welcome to the Grocery List App")
print(f"Current Date and Time: {date_time}")
print(f"You currently have {grocery_list[0]} and {grocery_list[1]} in your list.\n")

msg = input("Type of food to add to the grocery list: ").title().strip()
msg1 = input("Type of food to add to the grocery list: ").title().strip()
msg2 = input("Type of food to add to the grocery list: ").title().strip()

grocery_list.append(msg)
grocery_list.append(msg1)
grocery_list.append(msg2)

print(f"\nHere is your grocery list:\n{grocery_list}")
grocery_list.sort()
print(f"Here is your grocery list sorted:\n{grocery_list}")

print("\nSimulating grocery shopping...")

print(f"\nCurrent grocery list: {len(grocery_list)} items\n{grocery_list}")
new_item = input("What food did you just buy: ").title().strip()
print(f"Removing {new_item} from list...")
grocery_list.remove(new_item)

print(f"\nCurrent grocery list: {len(grocery_list)} items\n{grocery_list}")
next_item = input("What food did you just buy: ").title().strip()
print(f"Removing {next_item} from list...")
grocery_list.remove(next_item)

print(f"\nCurrent grocery list: {len(grocery_list)} items\n{grocery_list}")
next_item1 = input("What food did you just buy: ").title().strip()
print(f"Removing {next_item1} from list...")
grocery_list.remove(next_item1)
grocery_list.sort()

print(f"\nCurrent grocery list: {len(grocery_list)} items\n{grocery_list}")

print(f"\nSorry, the store is out of {grocery_list[-1]}")
Add_Newitem = input("What food would you like instead: ").title().strip()

grocery_list[-1] = Add_Newitem

# grocery_list.pop()
# grocery_list.insert(0, Add_Newitem)
# grocery_list = sorted(grocery_list, reverse = True)

grocery_list.reverse()

print(f"\nHere is what remains on your grocery list: \n{grocery_list}")




# SOl:2

# welcome screen
print("Welcome to Grocery List App")
from datetime import datetime as d

# date and time
date = d.now()
print(f'Current Date and Time {date.strftime("%m/%d %H:%M")}')

# list of items
grocery_list = ["Desi", "Cheese"]

# printing list
print(f"\nYou have {grocery_list[0]} and {grocery_list[1]} in your list.")

# addind food to the list
food_1 = str(input("\nWhat food you want to add: ")).capitalize()
food_2 = str(input("What food you want to add: ")).capitalize()
food_3 = str(input("What food you want to add: ")).capitalize()

# adding items to the list
grocery_list.append(food_1)
grocery_list.append(food_2)
grocery_list.append(food_3)

# showing list
print(f"\nHere is your grocery list: \n{grocery_list}")

# sorted grocery list
grocery_list.sort()
print(f"\nHere is your Grocery List sorted: \n{grocery_list}")

# kuchtobi
print("\nSimulating grocery shoping......")

# items in list length
print(f"\nCurrent item list is {len(grocery_list)} \n{grocery_list}")

# removing items
rem_1 = str(input("What did u buy: ")).capitalize()
grocery_list.remove(rem_1)
print(f"Removing {rem_1} from the list...")

# items in list length
print(f"\nCurrent item list is {len(grocery_list)} \n{grocery_list}")
rem_2 = str(input("\nWhat did u buy: ")).capitalize()
grocery_list.remove(rem_2)
print(f"Removing {rem_2} from the list...")

# items in list length
print(f"\nCurrent item list is {len(grocery_list)} \n{grocery_list}")
rem_3 = str(input("\nWhat did u buy: ")).capitalize()
grocery_list.remove(rem_3)
print(f"Removing {rem_3} from the list...")

# items in list length
print(f"\nCurrent item list is {len(grocery_list)} \n{grocery_list}")

# printing something
print(f"\nSorry the store is out of {grocery_list[-1]}: ")
new_item = str(input("What would u drink now: ")).capitalize()
grocery_list[-1] = new_item

# replacing meat with new one
print(f"\nHere is what remains {grocery_list}")

