#Sol 1:
#Welcome note
print("Welcome to the Voter Registration App\n")

name = input("Please enter your name: ").title().strip()
age = int(input("Please enter your age: "))

if age < 18:
    print("\nYou are not old enough to register to vote.")
else:
    print(f"\nCongratulations {name}! You are old enough to vote.")
    print("\nHere is a list of political parties to join.")
    print("\t- Republican")
    print("\t- Democratic")
    print("\t- Independent")
    print("\t- Libertarian")
    print("\t- Green")

    party = input("What party would you like to join: ").title().strip()
    msg = (f"\nCongratulations {name}! You have joined the {party} party!")

    if party == 'Democratic': 
        print(msg)
        print("That is a major party!")
    elif party == 'Green':
        print(msg)
        print("That is not a major party.")
    elif party == 'Republican':
        print(msg)
        print("This is a better party")
    elif party == 'Independent':
        print(msg)
        print("This is a bad party")
    elif party == 'Libertarian':
        print(msg)
        print("This is a worst party")
    else:
        pass


# Sol 2:
# welcom app
print('Welcom to the Voter Rgistration App')

# name
name = str(input('\nEnter your name: ')).lower().strip()
age = int(input('Enter your age: '))

#parties
parties = ['Red', 'Blue', 'Green', 'White', 'Purple']

# conditions
if age < 18:
    print('You are not old enough to register to vote.')
else:
    print(f'\nCongratulations {name} you are old enough.')
    print('\nHere are list of parties to join')

    # loop
    for p in parties:
        print(f'\t{p}')

    # user choice
    choice = str(input('\nWhat party would you like to join: ')).title().strip()

    # conditions
    if choice == 'Red':
        print(f'\nCongratulations {name} you have joined {choice} party!')
        print('That is a major party')
    elif choice == 'Blue':
        print(f'\nCongratulations {name} you have joined {choice} party!')
        print('That is a major party')
    elif choice == 'Green':
        print(f'\nCongratulations {name} you have joined {choice} party!')
        print('That is a major party')
    elif choice == 'White':
        print(f'\nCongratulations {name} you have joined {choice} party!')
        print('That is not a major party')
    else:
        print(f'\nCongratulations {name} you have joined {choice} party!')
        print('That is not a major party')
