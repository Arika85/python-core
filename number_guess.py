import random

#Welcome note
print("Welcome to the Guess My Number App\n")

name = input("Hello! What is your name: ").title().strip()
print(f"Well {name}, I am thinking of a number between 1 and 20.")

num = random.randint(1,20)

for count in range(1,6):
    guess = int(input("\nTake a guess: "))
    if guess < num:
        print("Your guess is too low")
    elif guess > num:
        print("Your guess is too high")
    else:
        break
        

if guess == num:
    print(f"\nGood job {name}! You guessed my number in {count} guesses!")
else:
    print(f"\nGame Over.  The number I was thinking of was {num}")