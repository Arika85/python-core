#Welcome Note
print("Welcome to the Basketball Roster Program\n")

#inputs for players
point = input("Who is your point guard: ").capitalize().strip()
shoot = input("Who is your shooting guard: ").capitalize().strip()
small = input("Who is your small forward: ").capitalize().strip()
power = input("Who is your power forward: ").capitalize().strip()
center = input("Who is your center: ").capitalize().strip()

players = ['point', 'shoot', 'small', 'power', 'center']

#printing the results
print(f"\n\tYour Starting {len(players)} for the upcoming basketball season")
print(f"\t\tPoint Guard:\t\t{point}")
print(f"\t\tShooting Guard:\t\t{shoot}")
print(f"\t\tSmall Forward:\t\t{small}")
print(f"\t\tPower Forward:\t\t{power}")
print(f"\t\tCenter:\t\t\t{center}")

# end note
print(f"\nOh no!, {small} is injured.")

# removing injured player
players.remove('small')

# diplaying remaining length of players
print(f"Your roster only has {len(players)} players.")

# replacing small forward player
small = input(f"Who will take {small}'s spot: ").title().strip()
players.append(small)

#adding new player and printing the results
print(f"\n\tYour Starting {len(players)} for the upcoming basketball season")
print(f"\t\tPoint Guard:\t\t{point}")
print(f"\t\tShooting Guard:\t\t{shoot}")
print(f"\t\tSmall Forward:\t\t{small}")
print(f"\t\tPower Forward:\t\t{power}")
print(f"\t\tCenter:\t\t\t{center}")

# end note
print(f"\nGood Luck {small} you will do great!")
print(f"Your roster now has {len(players)} players.")

