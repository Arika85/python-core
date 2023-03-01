
# # sol: 1          using def function

import random
print("Welcome to the Python Dice App\n")

def dice_app(sides,count_dice):
    print(f"\nYou rolled {count_dice} {sides}-sided dice")
    print("----Results are as followed----")
    result = []
    for i in range(count_dice):
        i = random.randint(1, sides)
        print(f"\t{i}")
        result.append(i)
    
    print(f"\nThe total value of your roll is {sum(result)}")

flag = True
while flag:
    sides = int(input("How many sides would you like on your dice: "))
    count_dice = int(input("How many dice would you like to roll: "))

    dice_app(sides,count_dice)
    ques = input("\nWould you like to roll again(y/n): ").lower()
    if ques != 'y':
        flag = False
        print("Thank you for using the Python Dice App")
        
# print("*******************************************************************")


# Sol: 2        Using while loop (random.choice)

import random
print("Welcome to the Python Dice App\n")

flag = True
while flag:
    sides = int(input("How many sides would you like on your dice: "))
    count_dice = int(input("How many dice would you like to roll: "))

    print(f"\nYou rolled {count_dice} {sides}-sided dice")

    #generating numbers in len of side and storing in an empty list
    s = []                                  # total = []
    for i in range(1, sides):                # for i in range(1,sides): 
        i +=1                                      # total += i 
        s.append(i)

    print(f"\n----Results are as followed----")
    #iterating through appended list with random choice
    j = []
    for i in range(count_dice):
        # i = random.choice(s)
        j.append(i)
        print(f"\t{i}")
    
    print(f"\nThe total value of your roll is {sum(j)}")
    ques = input("\nWould you like to roll again(y/n): ").lower()
    if ques != 'y':
        flag = False
        print("Thank you for using the Python Dice App")



print("*******************************************************************")

# # Sol:3     Using while loop (random.randint)

import random
print("Welcome to the Python Dice App\n")

flag = True
while flag:
    sides = int(input("How many sides would you like on your dice: "))
    count_dice = int(input("How many dice would you like to roll: "))

    print(f"\nYou rolled {count_dice} {sides}-sided dice")
    print("----Results are as followed----")
    result = []
    for i in range(count_dice):
        i = random.randint(1, sides)
        print(f"\t{i}")
        result.append(i)
    
    print(f"\nThe total value of your roll is {sum(result)}")
    ques = input("\nWould you like to roll again(y/n): ").lower()
    if ques != 'y':
        flag = False
        print("Thank you for using the Python Dice App")
        

print("*******************************************************************")






