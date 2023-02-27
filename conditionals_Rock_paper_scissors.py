import random

#welcome note
print("Welcome to a game of Rock, Paper, Scissors")
rounds = int(input("\nHow many rounds would you like to play: "))

# listing options in a variable (computer)
computer = ['rock', 'paper', 'scissors']
comp = random.choice(computer)      # choosing randomly from computer list

# initializing player and computer for counts
Player = 0  
Computer = 0

for round in range(rounds):
    round +=1           # increasing rounds
    print(f"\nRound {round}")
    print(f"Player: {Player}\t\tComputer: {Computer}")      # adding points to Player and Computer
    player = input("Time to pick...rock, paper, scissors: ").strip()
    print(f"\tComputer: {comp}")
    print(f"\tPlayer: {player}")
    if comp == player:
        print("\tIt is a tie, how boring!")
        print("\tThis round was a tie.")
    elif player == 'scissors' and comp == 'rock':
        print(f"\t{comp} wins {player}!")
        print(f"\tComputer win round {round}.")
        Computer +=1                             # As computer wins, adding 1 point to initialized Computer
    elif player == 'rock' and comp == 'paper':
        print(f"\t{comp} covers {player}!")
        print(f"\tComputer win round {round}.")
        Computer +=1                            # As computer wins, adding 1 point to initialized Computer
    elif player == 'paper' and comp == 'scissors':
        print(f"\t{comp} cut {player}!")
        print(f"\tComputer win round {round}.")
        Computer +=1                            # As computer wins, adding 1 point to initialized Computer
    elif player == 'paper' and comp == 'rock':
        print(f"\t{player} covers {comp}!")
        print(f"\tPlayer win round {round}.")
        Player +=1                              # As Player wins, adding 1 point to initialized Player
    elif player == 'scissors' and comp == 'paper':
        print(f"\t{player} cut {comp}!")
        print(f"\tPlayer win round {round}.")
        Player +=1                              # As Player wins, adding 1 point to initialized Player
    elif player == 'rock' and comp == 'scissors':
        print(f"\t{player} wins {comp}!")
        print(f"\tPlayer win round {round}.")
        Player +=1                              # As Player wins, adding 1 point to initialized Player
    else:
        print("\tThat is not a valid game option!")
        print("\tComputer gets the point")
        Computer +=1                     # As invalid, Computer gets 1 point and added to initialized Computer

# final results summary   
print("\nFinal Game Results")
print(f"\tRounds played: {rounds}")
print(f"\tPlayer Score: {Player}")
print(f"\tComputer Score: {Computer}")

# displaying winner 
if Computer > Player:
    print("\tWinner: Computer :-(")
else:
    print("\tWinner: Player :-)")


# Sol 2:

# welcome screen
import random
print('Welcom to a game of Rock, Paper, Scissors.')

# user input
rounds = int(input('\nHow many rounds you want to play: '))

# stored values
computer = 0
Player = 0
Round = 0
computer_in = ['Rock', 'Paper', 'Scissors']

# game rules and messages
s = '\tScissors cut Paper'
r = '\tRock crushes Scissors'
p = '\tPaper covers Rock'
tie = '\tIt\'s a tie, how boaring \n\tThis round was tie.'


# loops
for i in range(rounds):
    Round += 1
    print(f'\nRound {Round}')
    print(f'Player: {Player} \t Computer: {computer}')

    user_in = str(input('Time to pick Rock, Paper, Scissors: ')).title().strip()
    computer_coice = random.choice(computer_in)

    print(f'\tComputer: {computer_coice} \n\tPlayer: {user_in}')

    # code for tie
    # if user_in == 'Rock' and computer_coice == 'Rock':
    #     print(tie)
    # elif user_in == 'Paper' and computer_coice == 'Paper':
    #     print(tie)
    # elif user_in == 'Scissors' and computer_coice == 'Scissors':
    #     print(tie)

    # or we can also do
    if user_in == computer_coice:
        print(tie)


    #code if user wins
    elif user_in == 'Scissors' and computer_coice == 'Paper':
        Player+=1
        print(s)
        print(f'\tYou win round {Round}')
    elif user_in == 'Rock' and computer_coice == 'Scissors':
        Player+=1
        print(r)
        print(f'\tYou win round {Round}')
    elif user_in == 'Paper' and computer_coice == 'Rock':
        Player+=1
        print(p)
        print(f'\tYou win round {Round}')

    # code if computer wins
    elif computer_coice == 'Scissors' and user_in == 'Paper':
        computer+=1
        print(s)
        print(f'\tComputer win\'s round {Round}')
    elif computer_coice == 'Rock' and user_in == 'Scissors':
        computer+=1
        print(r)
        print(f'\tComputer win\'s round {Round}')
    elif computer_coice == 'Paper' and user_in == 'Rock':
        computer+=1
        print(p)
        print(f'\tComputer win\'s round {Round}')
    
    # if user input is invalid
    elif user_in != 'Rock' or 'Paper' or 'Scissors':
        print('\tThat\'s not a valid game option. \n\tComputer get\'s the point.')
        computer+=1

# final game results
print('\nFinal Game Results')
print(f'\tRound Played: {Round}')
print(f'\tPlayer Score: {Player}')
print(f'\tComputer Score: {computer}')
if computer < Player:
    print('\tWinner: Player :)')
elif computer == Player:
    print('\tTie again :(')
else:
    print('\tWinner: Computer :(')

